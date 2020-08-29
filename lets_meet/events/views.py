from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView


def home_page_view(request):
    return HttpResponse('Hello, world!')

# Create your views here.
