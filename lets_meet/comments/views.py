from django.shortcuts import render
from django.views.generic import DeleteView, CreateView, DetailView, View

from events.models import Event
from .models import Comment
# Create your views here.

class CommentDelete(DeleteView):
    model = Comment
    template_name = 'comments/delete.html'
    #TODO delete.html

class CommentDetail(DetailView):
    model = Comment
    template_name = 'comments/detail.html'
    #TODO detail.html

#TODO reply


