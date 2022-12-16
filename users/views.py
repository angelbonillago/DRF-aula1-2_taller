from django.shortcuts import render

from rest_framework import generics, status
from .serializers import SignUpSerializador,GetUserSerializador
from rest_framework.response import Response
from rest_framework.views import APIView
from .tokens import create_jwt_pair_for_user
from django.contrib.auth import authenticate
from rest_framework import viewsets
from .models import User


# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class=SignUpSerializador
    def post(self,request):
        data=request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response ={
                "message":"Usuario creado",
                "data":serializer.data
            }

            return Response(data=response,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self,request):
        email= request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email,password=password)
        if user is not None:
            #crear el token
            token=create_jwt_pair_for_user(user)

            response = {
                "message": "Logeado correctamente",
                 "email": email ,
                 "tokens": token
                }
            return Response(data=response,status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Correo inválido o contraseña incorrecta"})
        

    def get(self, request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)


class GetUser(viewsets.ReadOnlyModelViewSet):
    serializer_class=GetUserSerializador
    queryset=User.objects.all()
