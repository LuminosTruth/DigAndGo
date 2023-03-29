from django.shortcuts import render
from django.urls import reverse


def home(request):
    current_page = 'home'
    return render(request, 'main/landing.html', {'current_page': current_page})


def tech(request):
    current_page = 'tech'
    return render(request, 'main/tech.html', {'current_page': current_page})


def equipment(request):
    current_page = 'equipment'
    return render(request, 'main/equipment.html', {'current_page': current_page})


def company(request):
    current_page = 'company'
    return render(request, 'main/company.html', {'current_page': current_page})


def contacts(request):
    current_page = 'contacts'
    return render(request, 'main/contacts.html', {'current_page': current_page})
