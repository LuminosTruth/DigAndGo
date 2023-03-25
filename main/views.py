from django.shortcuts import render


def home(request):
    return render(request, 'main/landing.html')


def tech(request):
    return render(request, 'main/tech.html')


def equipment(request):
    return render(request, 'main/equipment.html')


def company(request):
    return render(request, 'main/company.html')


def contacts(request):
    return render(request, 'main/contacts.html')
