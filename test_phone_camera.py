import cv2

cap = cv2.VideoCapture("http://100.119.27.109:8080/video")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Unable to connect.")
        break
    cv2.imshow("Phone Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
