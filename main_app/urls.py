from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("dreams/", views.dreams_index, name="index"),
    path("dreams/<int:dream_id>", views.dreams_detail, name="detail"),
    path("dreams/create", views.DreamCreate.as_view(), name="dreams_create"),
]