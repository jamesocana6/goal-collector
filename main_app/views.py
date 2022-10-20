from django.shortcuts import render, redirect
from .models import Dream, Resource
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
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
    resources = Resource.objects.all()
    step_form = StepForm()
    return render(request, "dreams/detail.html", {
        "dream": dream,
        "step_form": step_form,
        "resources": resources,
    })

def add_step(request, dream_id):
    form = StepForm(request.POST)
    if form.is_valid():
        new_step = form.save(commit=False)
        new_step.dream_id = dream_id
        new_step.save()
    return redirect("detail", dream_id=dream_id)

def assoc_resource(request, dream_id, resource_id):
  # Note that you can pass a toy's id instead of the whole object
   Dream.objects.get(id=dream_id).resources.add(resource_id)
   return redirect('detail', dream_id=dream_id)

class DreamCreate(CreateView):
    model = Dream
    fields = ["name", "description", "timeline"]

class DreamUpdate(UpdateView):
    model = Dream
    fields = ["name", "description", "timeline"]

class DreamDelete(DeleteView):
    model = Dream
    success_url = "/dreams/"

class ResourceList(ListView):
    model = Resource
    template_name = "resources/index.html"

class ResourceDetail(DetailView):
    model = Resource
    template_name = "resources/detail.html"

class ResourceCreate(CreateView):
    model = Resource
    fields = "__all__"

class ResourceUpdate(UpdateView):
    model = Resource
    fields = "__all__"

class ResourceDelete(DeleteView):
    model = Resource
    success_url = "/resources/"