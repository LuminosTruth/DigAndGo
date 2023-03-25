from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="landing-page"),
    path('company/', company, name="company"),
    path('tech/', tech, name="tech"),
    path('equipment/', equipment, name="equipment"),
    path('contacts/', contacts, name="contact"),
    path('contacts/', contacts, name="contacts")
]
