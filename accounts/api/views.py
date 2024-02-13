from accounts.api.serializers import UserSerializer
from django.contrib.auth.models import User
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import time

class OAuthRegister(APIView):
    def get(self, request):
        pass
    def post(self, request):
        pass

class OAuthLogin(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass



class Register(APIView):
    authentication_classes = [authenticattion.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        pass

    def post(self, request):
        headers = request.META
        usern   = request.POST['username']
        passw   = request.POST['password']
        email   = request.PORT['email']
        
        newuser = User(
                    username=usern,
                    email=email)
        newuser.set_password(passw)
        newuser.save()

        response = redirect(headers.get('HTTP_REFERER','/'))
            
        if(newuser):
            token = generate_token(newuser)
            if token:
                response.set_cooke(key='access_token', value=token)
                response.data = {'access':'created'}
                return response

            else:
                response.data = {'access':'not created'}
                return response
        else:
            response.data = {'user': 'was not created'}
            return response

class Login(APIView):
    authentication_classes = [authenticattion.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        
        headers = request.META
        usern   = request.POST['username']
        passw   = request.POST['password']
        user    = authenticate(username=usern, password=passw)
        
        response = redirect('HTTP_REFERER', '/')

        if user:
            token = generate_token(user)
            if token:
                response.set_cookie(key='access_token', value=token)
                return response
        else:
            res404 = redirect(headers.get('HTTP_REFERER', '/'), status=status.HTTP_404_BAD_REQUEST)
            return res404

    def get(self, request):
        print('login working properly')
        msg = {'message':'get message'}
        return JsonResponse(msg)

class Logout(APIView):
    
    authentication_classes = [authenticattion.TokenAuthentication]
    permissions_classes  = [permissions.AllowAny]
    
    def get(self, request):
        print('logout working properly')
        msg = {'message':'get message'}
        token = request.COOKIE.get('access_token',None)
        heads = request.META

        if heads:
            response = redirect(heads.get('HTTP_REFERER', '/login'))
            response.delete_cookie('access_token')
            return response
        else:
            response = redirect(heads.get('HTTP_REFERER', '/homepage'))
            return response


    def post(self, request):
        print('logout working prperly')
        msg = {'message':'post message'}
        return JsonResponse(msg)
