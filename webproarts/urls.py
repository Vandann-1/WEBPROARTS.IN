from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from webproarts.sitemap import * # Ensure BlogSitemap is ready
from django.views.generic import TemplateView
from django.conf import settings

# Include both static pages and blog posts for full SEO coverage
sitemaps = {
    'static': StaticSitemap,
    'blog': BlogSitemap, 
}

urlpatterns = [
    path('admin/', admin.site.urls),



# Change 'sitemap.xml' to 'sitemap-new.xml'
    path('sitemap-new.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
    # Update robots.txt to point to the new name
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt",
        content_type="text/plain",
        extra_context={"site_url": "https://webproarts.in"}
    )),

    path('', include('web.urls')),
]