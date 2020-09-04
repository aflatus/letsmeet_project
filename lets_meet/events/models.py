from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    details = HTMLField('Details')
    venue = models.CharField(max_length=200)
    date = models.DateField(help_text='Required format: <em>YYYY-MM-DD</em>.')
    time = models.TimeField(help_text='Required format: <em>HH:MM:SS<em>')
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='participating', blank=True)
    num_of_participants = models.PositiveIntegerField(default=0, blank=True)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category, related_name='events')

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'
        ordering = ['date', 'time']

    def __str__(self):
        return self.name

    def get_abs_url(self):
        return reverse('events:event-detail', kwargs={'pk': self.pk})

    def get_number_of_participants(self):
        return self.participants.all().count()

# Create your models here.
