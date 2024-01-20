from django.urls import path

from accounts.api.views import login, logout

appname = 'usersapi'

urlpattern = [
        path('/user/login/',    login.as_view(), name='login'),
        path('/user/logout/',   logout.as_view(), name='logout')
]


