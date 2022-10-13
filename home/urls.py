from django.urls import path
from . import views

urlpatterns = [
    path('mock/', views.mock)
]