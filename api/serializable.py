from rest_framework import serializers
from students.models import Student
from django.contrib.auth.models import User
class serializer_students(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"

class User_Serializar(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'password', 'email']
    
# class serializer_dish(serializers.ModelSerializer):
#     # user=User_Sesheerializar()
#     class Meta:
#         model=dish
#         fields=["id","dishName","price"]
#     def validate_price(self,price):# as you can in the function after the validate add _ and add the column(price) that acces it
#         if price < 100:
#             raise serializers.ValidationError("Price should be gretter than 100")
#         return price
#     def validate(self,data):
#         speacial="!@#$%^&*()_?"
#         if any( c in speacial for c in data["dishName"]):
#             raise serializers.ValidationError("speacial character Not allowed")
#         return data
# class serializer_order(serializers.ModelSerializer):
#     class Meta:
#         model=orders
#         fields="__all__"
# class LoginSerializer(serializers.Serializer):
#     email=serializers.EmailField()
#     password=serializers.CharField()