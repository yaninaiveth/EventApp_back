from accounts.api.serializers import UserSerializer
from django.contrib.auth.models import User
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class login(APIView):
    def get(self, resquest):
        #userobjects = User.objects.all()
        #serializer = UserSerializer(userobjects)
        print('login working properly')
        #return Response(serializer.data)
        msg = {'message':'get message'}
        return JsonResponse(msg)

    def post(self, request):
        print('login working properly')
        msg = {'message':'post message'}
        return JsonResponse(msg)

class logout(APIView):
    
    def get(self, request):
        print('logout working properly')
        msg = {'message':'get message'}
        return JsonResponse(msg)

    def post(self, request):
        print('logout working prperly')
        msg = {'message':'post message'}
        return JsonResponse(msg)
