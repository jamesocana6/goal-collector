from django.db import models
from django.urls import reverse

class Dream(models.Model): 
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    steps = models.TextField(max_length=255)
    timeline = models.IntegerField()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={'dream_id': self.id})
    
