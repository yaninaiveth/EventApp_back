from django.shortcuts import render
from django.views.generic import View
from .forms import PostCreateForm

# Lista los eventos
class EventListView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'event_list.html', context)

# Vista del form para crear el evento
class EventCreateView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'event_create.html', context)
    def post(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'event_create.html', context)


