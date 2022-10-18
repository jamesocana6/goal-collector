from django.shortcuts import render
from .models import Dream
from django.views.generic.edit import CreateView

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def dreams_index(request):
    dreams = Dream.objects.all()
    return render(request, "dreams/index.html", {"dreams": dreams})

def dreams_detail(request, dream_id):
    dream = Dream.objects.get(id = dream_id)
    return render(request, "dreams/detail.html", {"dream": dream})

class DreamCreate(CreateView):
    model = Dream
    fields = "__all__"
