from django.shortcuts import render
from django.views.generic import ListView , DeleteView ,UpdateView , DetailView , CreateView
from django.urls import reverse_lazy, reverse
from .models import Roses




class RosesListView(ListView):
    template_name = 'roses/list_view.html'
    model=Roses
    
class RosesDetailView(DetailView):
    template_name='roses/detail_view.html'
    model=Roses 
    


class RosesCreateView(CreateView):
    template_name='roses/create_view.html'
    model=Roses
    fields = ['title', 'purchaser', 'description']

class RosesUpdateView(UpdateView):
    template_name='roses/update_view.html'
    model=Roses
    fields = ['title', 'purchaser', 'description']

class RosesDeleteView(DeleteView):
    template_name='roses/delete_view.html'
    model=Roses
    success_url = reverse_lazy('roses') # when i delete , i will be redirected to homepage