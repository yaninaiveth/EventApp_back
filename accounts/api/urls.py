from django.urls import path

from accounts.api.views import Login, Logout, Registe, OAuthLogin, OAuthRegister

app_name = 'usersapi'

urlpatterns = [
        #oauth authentication
        path('oauth/login/',        OAuthLogin.as_view(), name='oauthlogin'),
        path('oath/register/',      OAuthRegister.as_view(), name='oauthregister'),
        
        path('register/',           Register.as_view(), name='register'),
        path('login/',              Login.as_view(), name='login'),
        path('logout/',             Logout.as_view(), name='logout')
]


