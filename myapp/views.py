from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Company
from django.urls import reverse_lazy

'''
def index(request):
	return render(request, 'home.html', {})
'''


class HomeView(ListView):
	model = Company 
	template_name = 'home.html'

class AddCompView(CreateView):
	model = Company
	template_name = 'add.html'
	fields = '__all__'

class UpdatePostView(UpdateView):
	model = Company
	template_name="edit.html"
	fields= '__all__'

class DeletePostView(DeleteView):
	model = Company
	template_name = "delete.html"
	success_url = reverse_lazy('home')