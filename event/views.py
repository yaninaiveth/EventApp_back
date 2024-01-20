from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import PostCreateForm
from .models import EventPost

# Lista los eventos
class EventListView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'event_list.html', context)

# Vista del form para crear el evento
class EventCreateView(View):
    def get(self, request, *args, **kwargs):
        form=PostCreateForm()
        context={
            'form':form
        }
        return render(request, 'event_create.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method=="POST":

            form = PostCreateForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get('name')
                description = form.cleaned_data.get('description')

                p, created = EventPost.objects.get_or_create(name=name, description=description)
                p.save()
                return redirect('event:home')
        context={
            
        }
        return render(request, 'event_create.html', context)


