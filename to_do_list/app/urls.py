from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('update/<str:pk>/', views.update_task),
    path('delete/<str:pk>/', views.delete_task),
]