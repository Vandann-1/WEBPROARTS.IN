from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from webproarts.sitemap import*
from django.views.generic import TemplateView
from django.conf import settings

sitemaps = {
    'static': StaticSitemap,
    'blog': BlogSitemap, 
}

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1. SITEMAP: Using the new name to bypass Google's old cache
    path('sitemap-new.xml', sitemap, {'sitemaps': sitemaps}, 
         name='django.contrib.sitemaps.views.sitemap'),

    # 2. ROBOTS.TXT: MUST be named 'robots.txt' so Google can find it
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt",
        content_type="text/plain",
        extra_context={"site_url": "https://www.webproarts.in"}
    )),

    path('', include('web.urls')),
]