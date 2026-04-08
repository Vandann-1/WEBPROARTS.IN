from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return [
            'home',
            'about',
            'contact_page',
            'blogs',
            'digital_marketing',
            'web_design',
            'video_editing',
            'social_media',
            'privacy_policy',
            'terms_of_service',
            'graphic_design',
            'blog_detail',
        ]

    def location(self, item):
        return reverse(item)