from django.urls import path
from .views import EventListView, EventCreateView

app_name="event"

urlpatterns = [
    path('', EventListView.as_view(), name="home"),
    path('create/', EventCreateView.as_view(), name="create")
]
