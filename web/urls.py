
from django import views
from django.contrib import admin
from django.urls import path
from web.views import *



# urlpatterns = [    path('admin/', admin.site.urls),
#                path("",home, name="home"),
#                path("about/", about, name="about")
#                ,
#                 path("contac/", contact, name="contac")
#                 ,path("digital-marketing/", digital_marketing, name="digital_marketing")
#                 ,path("web-design/", web_design, name="web_design")
#                 ,path("video-editing/", video_Editing, name="video_editing")
#                 ,path("social-media/", social_media, name="social_media")
#                 ,path("graphic-design/", garphic_design, name="graphic_design")
#                 ,path("privacy-policy/",policy, name="privacy_policy"),
#                 path("terms-of-service/",policy, name="terms_of_service"),
#                 path('contact/', contact, name='contact-us'),
#                 path('web-development-websites/', webdev, name='webdev'),
#                 path('contact/', contact_view, name='contact_form')
            

#                 # Dynamic Detail Page (The "Slug" is the magic part)
#                 ,path('blogs/', blogs, name='blogs'), 
    
#                path('blogs/<int:post_id>/', blog_detail, name='blog_detail'),

                
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("about/", about, name="about"),
    
    # RENAME or REMOVE the duplicates. 
    # Let's keep one clear path for the form submission.
    path("contact.html/", contact, name="contact.html"), # The page itself
    path("contact-submit/", contact_view, name="contact_form"), # The AJAX logic 
    
    path("digital-marketing/", digital_marketing, name="digital_marketing"),
    path("web-design/", web_design, name="web_design"),
    path("video-editing/", video_Editing, name="video_editing"),
    path("social-media/", social_media, name="social_media"),
    path("graphic-design/", garphic_design, name="graphic_design"),
    path("privacy-policy/", policy, name="privacy_policy"),
    path("terms-of-service/", policy, name="terms_of_service"),
    path('web-development-websites/', webdev, name='webdev'),
    
    path('blogs/', blogs, name='blogs'), 
    path('blogs/<int:post_id>/', blog_detail, name='blog_detail'),
]