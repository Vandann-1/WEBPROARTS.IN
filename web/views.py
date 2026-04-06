from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']       
        message = request.POST['message']
        # send email
        from django.core.mail import send_mail
        subject = f"New message from {first_name} {last_name}"

        message = f"Name: {first_name} {last_name}\nEmail: {email}\nMessage: {message}"
        send_mail(subject, message, 'from@example.com', ['to@example.com'])
    return render(request, 'contact.html')



from django.http import JsonResponse
import json
from django.core.mail import send_mail

def contact_form(request):
    if request.method == "POST":
        try:
            if not request.body:
                return JsonResponse({"error": "Empty request body"}, status=400)

            data = json.loads(request.body)

            first_name = data.get("first_name")
            last_name = data.get("last_name")
            email = data.get("email")
            subject = data.get("subject")
            message = data.get("message")

            if not email or not message:
                return JsonResponse({"error": "Missing required fields"}, status=400)

            full_message = f"""
New Inquiry from WebProArts Website

Name: {first_name} {last_name}
Email: {email}
Service: {subject}

Message:
{message}
"""

            send_mail(
                subject=f"New Client Inquiry - {subject}",
                message=full_message,
                from_email="webproarts@gmail.com",
                recipient_list=["webproarts@gmail.com"],
                fail_silently=False,
            )

            return JsonResponse({"status": "success"})

        except Exception as e:
            print("ERROR:", e)  # 🔥 IMPORTANT
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)


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