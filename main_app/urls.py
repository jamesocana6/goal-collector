from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("dreams/", views.dreams_index, name="index"),
    path("dreams/<int:dream_id>", views.dreams_detail, name="detail"),
    path("dreams/create", views.DreamCreate.as_view(), name="dreams_create"),
    path("dreams/update/<int:pk>", views.DreamUpdate.as_view(), name="dreams_update"),
    path("dreams/delete/<int:pk>", views.DreamDelete.as_view(), name="dreams_delete"),
    path("dreams/<int:dream_id>/add_step", views.add_step, name="add_step"),
]