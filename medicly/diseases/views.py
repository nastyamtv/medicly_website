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

from django.shortcuts import render
import random  # Поки що рандомний результат для тесту

def pneuscan_view(request):
    result = None

    if request.method == "POST" and request.FILES.get("file"):
        # Симуляція аналізу: випадковий результат "Хворий" або "Не хворий"
        result = random.choice(["Хворий", "Не хворий"])

    return render(request, 'pneuscan.html', {"result": result})



import openai
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

openai.api_key = "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"  # Використовуй свій OpenAI API ключ

# Відображення сторінки
def mediclybot_view(request):
    return render(request, "mediclybot.html")

# Обробка повідомлень у чаті
#@csrf_exempt
def mediclybot_api(request):
    if request.method == "POST":
        try:
            #return JsonResponse({"response": "Hello"}) # for debug
            data = request.POST["data"]
            data = json.loads(data)
            user_message = data["message"]
            # Запит до OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_message}]
            )
            return JsonResponse({"response": user_message})
            #return JsonResponse({"response": response["choices"][0]["message"]["content"]})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Метод не підтримується"}, status=405)

