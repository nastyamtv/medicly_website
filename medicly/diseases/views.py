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



from django.shortcuts import render

def mediclybot_view(request):
    response_text = ""
    if request.method == "POST":
        symptoms = request.POST.get("symptoms")
        response_text = rule_based_response(symptoms)
    return render(request, "mediclybot.html", {"response": response_text})

def rule_based_response(symptoms):
    s = symptoms.lower()

    if "кашель" in s or "задишка" in s or "чхання" in s:
        return "Можливо у вас грип, застуда або пневмонія. Бажано звернутись до лікаря або зробити рентген."

    elif "голова" in s or "нудота" in s or "запаморочення" in s:
        return "Це може бути мігрень, отруєння або гіпотонія. Пийте воду, спробуйте відпочити."

    elif "температура" in s or "гарячка" in s or "озноб" in s:
        return "Підвищена температура часто свідчить про інфекційне захворювання. Рекомендовано зробити загальний аналіз крові."

    elif "живіт" in s or "болить живіт" in s or "діарея" in s:
        return "Симптоми вказують на проблеми з травленням, можливо отруєння або гастрит. Варто звернутись до гастроентеролога."

    elif "висип" in s or "почервоніння" in s or "свербіж" in s:
        return "Може бути алергія або шкірне захворювання. Уникайте алергенів, зверніться до дерматолога."

    elif "болить серце" in s or "тягне у грудях" in s or "пульс" in s:
        return "Серцеві симптоми — це серйозно. Якщо відчуваєте біль у грудях, негайно зверніться до швидкої допомоги."

    elif "нема сил" in s or "втома" in s or "сонливість" in s:
        return "Можливо, анемія або нестача вітамінів. Рекомендується здати загальний аналіз крові та перевірити рівень заліза."

    elif "депресія" in s or "тривога" in s:
        return "Симптоми можуть бути пов’язані з психологічним станом. Спробуйте поговорити з психологом."

    else:
        return "Не вдалося точно визначити проблему. Спробуйте описати симптоми інакше або зверніться до лікаря."



from django.shortcuts import render
from django.db.models import Q

from django.http import JsonResponse

def search(request):
    q = request.GET.get('q', '').strip()
    diseases = Disease.objects.filter(name__icontains=q) if q else Disease.objects.none()
    doctors  = Doctor.objects.filter(name__icontains=q)  if q else Doctor.objects.none()
    return render(request, 'search_results.html', {
        'query': q,
        'diseases': diseases,
        'doctors': doctors,
    })

def autocomplete(request):
    term = request.GET.get('term', '').strip()
    # Шукаємо в обох таблицях одночасно
    dis = Disease.objects.filter(name__icontains=term).values_list('name', flat=True)[:5]
    doc = Doctor .objects.filter(name__icontains=term).values_list('name', flat=True)[:5]
    return JsonResponse(list(dis) + list(doc), safe=False)


import os
import numpy as np
from django.conf import settings
from django.shortcuts import render
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


def pneuscan(request):
    if request.method != "POST":
        return render(request, "pneuscan.html", {"result": None})

    if not request.FILES.get("file"):
        return render(request, "pneuscan.html", {"result": "No file selected."})

    try:
        file = request.FILES["file"]
        upload_path = os.path.join(settings.BASE_DIR, 'temp_upload.jpg')
        with open(upload_path, 'wb+') as f:
            for chunk in file.chunks():
                f.write(chunk)

        model_path = os.path.join(settings.BASE_DIR, 'disease', 'pneumonia_model.h5')
        model = load_model(model_path)

        img = image.load_img(upload_path, target_size=(150, 150), color_mode='grayscale')
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0

        prediction = model.predict(img_array)
        probability = prediction[0][0]

        if probability > 0.5:
            result = "Normal (Pneumonia probability: {:.2f}%)".format(100 - probability * 100)
        else:
            result = "Pneumonia (Pneumonia probability: {:.2f}%)".format((1 - probability) * 100)

    except Exception as e:
        result = f"Error: {str(e)}"

    finally:
        if os.path.exists(upload_path):
            os.remove(upload_path)

    return render(request, "pneuscan.html", {"result": result})

