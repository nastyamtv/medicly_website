from django.urls import include, path

from diseases import views

#from diseases import views

urlpatterns = [
    path('', views.index),
    path('blog/', views.blog_diseases),
]