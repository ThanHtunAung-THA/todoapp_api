from django.shortcuts import render

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# Create your views here.
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
  def validate(self, attrs):
    data = super().validate(attrs)

    return data

class CustomTokenObtainPairView(TokenObtainPairView):
  serializer_class = CustomTokenObtainPairSerializer