from django.urls import path
from .views import EventListView, EventCreateView, EventDetailView

app_name="event"

urlpatterns = [
    path('', EventListView.as_view(), name="home"),
    path('create/', EventCreateView.as_view(), name="create"),
    path('<int:pk>/', EventDetailView.as_view(), name="detail"),
]
