from django.shortcuts import render, get_object_or_404

from diseases.models import Disease


from doctors.models import Doctor

def home(request):
    doctors = Doctor.objects.all()[:3]  # Вивести перших 3 лікарів
    return render(request, 'home.html', {'doctors': doctors})

def index(request):
    return render(request, 'index.html')

def blog_diseases(request):
    diseases = Disease.objects.all()
    context = {"diseases_list": diseases}
    return render(request, 'blog_diseases.html', context)

def disease_detail(request, disease_id):
    disease = get_object_or_404(Disease, id=disease_id)
    context = {"disease": disease}
    return render(request, 'disease_detail.html', context)



def blog_doctors(request):
    doctors = Doctor.objects.all()
    context = {"doctors_list": doctors}
    return render(request, 'blog_doctors.html', context)

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    context = {"doctor": doctor}
    return render(request, 'doctor_detail.html', context)

def mediclybot(request):
    return render(request, 'mediclybot.html')  # Створіть відповідний шаблон

