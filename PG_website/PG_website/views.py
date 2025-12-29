from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request, 'Home.html')

def About(request):
    return render(request, 'About.html')

def pg_list(request):
    return render(request, 'pg_list.html')

def Contact(request):
    return render(request, 'Contact.html')

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
