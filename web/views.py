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


