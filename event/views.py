from django.shortcuts import render
from django.views.generic import View

class EventListView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'event_list.html', context)
