from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact_api 

def Home(request):
    return render(request, 'Home.html')

def About(request):
    return render(request, 'About.html')

def pg_list(request):
    return render(request, 'pg_list.html')

# def Contact(request):
#     if request.method == "GET":
#         return render(request, "Contact.html")

#     if request.method == "POST":
#         data = json.loads(request.body)

#         Contact_api.objects.create(
#             name=data.get("name"),
#             email=data.get("email"),
#             phone=data.get("phone"),
#             message=data.get("message")
#         )

#         return JsonResponse({
#             "status": "success",
#             "message": "Contact saved successfully"
#         })

def Contact(request):
    if request.method == "POST":
        Contact_api.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            message=request.POST.get("message"),
        )
        return HttpResponse("Contact form submitted successfully")

    return render(request, "Contact.html")

# def Contact(request):
#     return render(request, "Contact.html")

def Service(request):
    pg_data = [
        {
            "name": "Comfort PG",
            "city": "Ahmedabad",
            "rent": 6000,
            "image": "pg1.jpg",
            "description": "Fully furnished PG for girls with food facility."
        },
        {
            "name": "Royal Stay PG",
            "city": "Surat",
            "rent": 7500,
            "image": "pg2.jpg",
            "description": "Safe PG for professionals."
        },
        {
            "name": "Home Away PG",
            "city": "Ahmedabad",
            "rent": 5000,
            "image": "pg3.jpg",
            "description": "Affordable PG with Wi-Fi."
        }
    ]
    return render(request, 'Service.html', {'pg_data': pg_data})

def FAQ(request):
    return render(request, 'FAQ.html')

def Feedback(request):
    return render(request, 'Feedback.html')
