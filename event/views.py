from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import PostCreateForm
from .models import EventPost

# Lista los eventos
class EventListView(View):
    def get(self, request, *args, **kwargs):
        posts = EventPost.objects.all()
        context={
            'posts':posts
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
    
# Vista para poder ver los modelos

class EventDetailView(View):
    def get(self, request, pk,  *args, **kwargs):
        post = get_object_or_404(EventPost, pk=pk)
        context={
            'post':post
        }
        return render (request, 'event_detail.html', context)
# Crear vista que nos permita eliminar el evento
# Crear vista para eliminar un evento
    

    

