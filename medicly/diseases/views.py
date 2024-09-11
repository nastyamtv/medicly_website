from django.shortcuts import render

from diseases.models import Disease


def index(request):
    return render(request, 'index.html')

def blog_diseases(request):
    diseases = Disease.objects.all()
    context = {"diseases_list": diseases}
    return render(request, 'blog_diseases.html', context)
