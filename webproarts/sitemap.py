from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from web.models import *  # Import your Blog model

class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        # Remove 'blog_detail' from here because it needs an ID/Slug
        return [
            'home', 'about', 'contact.html', 'blogs',
            'digital_marketing', 'web_design', 'video_editing',
            'social_media', 'privacy_policy', 'terms_of_service', 'graphic_design',
        ]

    def location(self, item):
        return reverse(item)

# Add this to include your actual blog posts!
class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return BlogPost.objects.all() # Or Post.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.updated_at # Helps Google know when you edited a post