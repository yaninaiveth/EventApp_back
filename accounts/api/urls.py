from django.urls import path

from accounts.api.views import login, logout

app_name = 'usersapi'

urlpatterns = [
        path('login/',    login.as_view(), name='login'),
        path('logout/',   logout.as_view(), name='logout')
]


