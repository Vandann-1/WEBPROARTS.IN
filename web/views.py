from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import ContactMessage

@csrf_protect
def contact_form_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            
            # Basic Validation
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            subject = data.get('subject')
            message = data.get('message', '')

            if not all([first_name, last_name, email, subject]):
                return JsonResponse({"status": "error", "error": "All fields are required."}, status=400)

            # Save to Database
            ContactMessage.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                subject=subject,
                message=message
            )

            return JsonResponse({"status": "success", "message": "Data saved successfully!"})

        except Exception as e:
            return JsonResponse({"status": "error", "error": str(e)}, status=500)
            
    return JsonResponse({"status": "error", "error": "Invalid request method"}, status=400)




def blogs(request):
    return render(request, 'blog.html')


def digital_marketing(request):
    return render(request, 'digital-marketing.html')

def web_design(request):
    return render(request, 'web-design.html')

def video_Editing(request):
    return render(request, 'video-editing.html')

def social_media(request):
    return render(request, 'social-media.html')

def policy(request):
    return render(request, 'policy.html')

def term(request):
    return render(request, 'term.html')