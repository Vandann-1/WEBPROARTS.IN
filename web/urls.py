
from django.contrib import admin
from django.urls import path
from web.views import *



urlpatterns = [    path('admin/', admin.site.urls),
               path("",home, name="home"),
               path("about/", about, name="about")
               ,path("blogs", blogs, name="blogs"),
                path("contact/", contact, name="contact")
                ,path("digital-marketing/", digital_marketing, name="digital_marketing")
                ,path("web-design/", web_design, name="web_design")
                ,path("video-editing/", video_Editing, name="video_editing")
                ,path("social-media/", social_media, name="social_media")
                ,path("privacy-policy/",policy, name="privacy_policy"),
                path("terms-of-service/",policy, name="terms_of_service"),
            

                path('contact-frm/', contact_form_view, name='contact_form_submit'),
]
                
