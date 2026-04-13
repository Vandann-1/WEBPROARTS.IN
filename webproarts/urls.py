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

    # Sitemap - This generates the XML for Google
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, 
         name='django.contrib.sitemaps.views.sitemap'),

    # Robots.txt - Served as a template to use your SITE_URL variable
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt",
        content_type="text/plain",
        extra_context={"site_url": settings.SITE_URL}
    )),

    path('', include('web.urls')),
]