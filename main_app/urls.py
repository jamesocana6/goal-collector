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
    path("resources/", views.ResourceList.as_view(), name="resources_index"),
    path("resources/<int:pk>", views.ResourceDetail.as_view(), name="resources_detail"),
    path("resources/create", views.ResourceCreate.as_view(), name="resources_create"),
    path("resources/update/<int:pk>", views.ResourceUpdate.as_view(), name="resources_update"),
    path("resources/delete/<int:pk>", views.ResourceDelete.as_view(), name="resources_delete"),
    path("resources/delete/<int:dream_id>/assco_resource/<int:resource_id>/", views.assoc_resource, name="assoc_resource"),
]