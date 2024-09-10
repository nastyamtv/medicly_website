from django.urls import include, path

from diseases import views

urlpatterns = [
    path('', views.index),
]