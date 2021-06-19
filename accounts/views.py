from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
# Create your views here.
def Home(request):
    return HttpResponse("<h1> Welcome To Home </h1>")

class RegisterView(APIView):

    def post(self , request):
        try:
            serializer = UserSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    'status': 403,
                    'errors': serializer.errors
                })
            serializer.save()
            return Response({'status':200 , 'message': 'an OTP sent on your number and email'})
        except Exception as e:
            print(e)
            return Response({'status' : 404 , 'error' : 'Somthing went Wrong'})