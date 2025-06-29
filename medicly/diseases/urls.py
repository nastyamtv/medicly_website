from django.urls import include, path

from diseases import views
#from diseases import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home, name='home'),


    path('diseases/', views.blog_diseases, name='diseases'),
    path('diseases/<int:disease_id>/', views.disease_detail, name='disease_detail'),
    path('doctors/', views.blog_doctors, name='doctors'),
    path('doctors/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('mediclybot/', views.mediclybot_view, name='mediclybot'),
    #path('pneuscan/', views.pneuscan_view, name='pneuscan'),
    path('pneuscan/', views.pneuscan, name='pneuscan'),
    path('search/', views.search, name='search'),




]