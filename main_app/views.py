from django.shortcuts import render, redirect
from .models import Dream
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import StepForm

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def dreams_index(request):
    dreams = Dream.objects.all()
    return render(request, "dreams/index.html", {"dreams": dreams})

def dreams_detail(request, dream_id):
    dream = Dream.objects.get(id = dream_id)
    step_form = StepForm()
    return render(request, "dreams/detail.html", {
        "dream": dream,
        "step_form": step_form,
    })

def add_step(request, dream_id):
    form = StepForm(request.POST)
    if form.is_valid():
        new_step = form.save(commit=False)
        new_step.dream_id = dream_id
        new_step.save()
    return redirect("detail", dream_id=dream_id)


class DreamCreate(CreateView):
    model = Dream
    fields = "__all__"

class DreamUpdate(UpdateView):
    model = Dream
    fields = "__all__"


class DreamDelete(DeleteView):
    model = Dream
    success_url = "/dreams/"