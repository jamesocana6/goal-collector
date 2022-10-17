from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

class Dream: 
    def __init__(self, name, description, steps, timeline = float("inf")): 
        self.name = name
        self.description = description
        self.steps = steps
        self.timeline = timeline

dreams = [
    Dream("Get a job", "get a job after bootcamp", "apply to at least 5 positions everyday", 3),
    Dream("Graduate bootcamp", "2 more projects!", "go to class, do your work", 1),
]

def dreams_index(request):
    return render(request, "dreams/index.html", {"dreams": dreams})