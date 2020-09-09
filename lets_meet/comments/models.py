from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

from events.models import Event


class Comment(models.Model):
    comment = models.TextField(max_length=500)
    creation_date = models.DateField(auto_now=True)
    creation_time = models.TimeField(auto_now=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('creation_date', 'creation_time')

    def __str__(self):
        return self.comment

    
# Create your models here.
