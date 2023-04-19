from django.contrib.sitemaps import Sitemap
from .urls import *


class MySitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return ['landing-page', 'company', 'tech', 'equipment', 'contact', 'contacts']

    def location(self, obj):
        return reverse(obj)
