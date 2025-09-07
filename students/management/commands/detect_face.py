from django.core.management.base import BaseCommand
from students.models import Student, Attendance, Subject
from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
import cv2
from django.utils import timezone
import time
from PIL import Image
import numpy as np

class Command(BaseCommand):
    help = 'Detect faces and mark attendance'

    def handle(self, *args, **options):
        known_face_encodings, known_face_ids = self.encode_uploaded_images()
        # further code for processing

    def encode_uploaded_images(self):
        known_encodings = []
        known_ids = []

        resnet = InceptionResnetV1(pretrained='vggface2').eval()

        for student in Student.objects.exclude(profile='profile_images/default.jpeg'):
            if student.profile and student.profile.name:  # Check if profile image exists
                try:
                    # Use the correct path relative to MEDIA_ROOT
                    image_path = student.profile.path
                    img = Image.open(image_path).convert('RGB')
                    img = img.resize((160, 160))
                    img_tensor = torch.tensor(np.array(img)).permute(2, 0, 1).float().unsqueeze(0) / 255.0

                    with torch.no_grad():
                        embedding = resnet(img_tensor).numpy()[0]
                        known_encodings.append(embedding)
                        known_ids.append(student.id)
                except Exception as e:
                    print(f"Error processing image for student {student.id}: {e}")

        return known_encodings, known_ids

    def process_frame(self, camera_index, known_face_encodings, known_face_ids):
        mtcnn = MTCNN(keep_all=True, device='cuda' if torch.cuda.is_available() else 'cpu')
        resnet = InceptionResnetV1(pretrained='vggface2').eval()

        cap = cv2.VideoCapture(camera_index)
        recently_seen = {}
        COOLDOWN_SECONDS = 60

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            boxes, _ = mtcnn.detect(frame_rgb)

            if boxes is not None:
                aligned_faces = []
                for box in boxes:
                    face = frame_rgb[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
                    if face.size == 0:
                        continue
                    face = cv2.resize(face, (160, 160))
                    face = torch.tensor(face).permute(2, 0, 1).float().unsqueeze(0) / 255.0
                    aligned_faces.append(face)

                for i, face in enumerate(aligned_faces):
                    embedding = resnet(face).detach().numpy()[0]
                    distances = [np.linalg.norm(embedding - known_enc) for known_enc in known_face_encodings]
                    min_distance = min(distances)
                    best_match_index = distances.index(min_distance)

                    student_id = None
                    if min_distance < 0.8:
                        student_id = known_face_ids[best_match_index]

                    box = boxes[i]
                    if student_id:
                        current_time = time.time()
                        last_seen = recently_seen.get(student_id, 0)

                        if current_time - last_seen > COOLDOWN_SECONDS:
                            recently_seen[student_id] = current_time
                            try:
                                student = Student.objects.get(id=student_id)
                                today = timezone.now().date()

                                subject = None
                                attendance, created = Attendance.objects.get_or_create(
                                    student=student,
                                    date=today,
                                    subject=subject
                                )
                                attendance.present = True
                                attendance.save()

                                success_msg = f"{student.name} marked present"
                                print(success_msg)
                                cv2.putText(frame, success_msg, (int(box[0]), int(box[1]) + 60),
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

                            except Student.DoesNotExist:
                                pass
                    else:
                        cv2.putText(frame, "Not Recognized", (int(box[0]), int(box[1]) - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

                    cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 255, 0), 2)

            cv2.imshow(f'Camera {camera_index}', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
