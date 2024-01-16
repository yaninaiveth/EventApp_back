from django.urls import path
from .views import EventListView

app_name="event"

urlpatterns = [
    path('', EventListView.as_view(), name="home")
]
