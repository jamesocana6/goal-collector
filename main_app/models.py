from django.db import models
from django.urls import reverse

class Resource(models.Model): 
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("resources_detail", kwargs={'pk': self.id})
    
class Dream(models.Model): 
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    timeline = models.IntegerField()
    resources = models.ManyToManyField(Resource)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={'dream_id': self.id})
    
class Step(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)

    dream = models.ForeignKey(Dream, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}: {self.description}"

