from rest_framework.decorators import api_view
from rest_framework.response import Response
from students.models import Student 
from .serializable import serializer_students
from django.contrib.auth.models import User
from rest_framework.views import APIView
@api_view(["GET"])
def all_api(request):
    content={
        "api/Students":"all_students", 
        "api/students/id":"specific_restaurants",
        # "api/dishes":"all_dishes",
        # "api/dishes/id":"specific_dishes",
        # "api/user":"all_User"
    }
    return Response(content)    

class studentAPI(APIView):
    def get(self,request):
        obj=Student.objects.all()
        serializer=serializer_students(obj,many=True)
        return Response(serializer.data)    
 