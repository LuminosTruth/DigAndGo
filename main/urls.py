from django.urls import path
from .views import *
from django.contrib.sitemaps.views import sitemap
from .sitemaps import MySitemap

sitemaps = {
    'my_model': MySitemap,
}

urlpatterns = [
    path('', home, name="landing-page"),
    path('company/', company, name="company"),
    path('tech/', tech, name="tech"),
    path('equipment/', equipment, name="equipment"),
    path('contacts/', contacts, name="contact"),
    path('contacts/', contacts, name="contacts"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]
