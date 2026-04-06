from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from webproarts.sitemap import StaticSitemap
from django.views.generic import TemplateView
from django.conf import settings

sitemaps = {
    'static': StaticSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),

    # Sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),

    # Robots.txt
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt",
        content_type="text/plain",
        extra_context={"site_url": settings.SITE_URL}
    )),

    path('', include('web.urls')),
]