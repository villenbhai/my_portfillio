from django.shortcuts import render, redirect
from .forms import PhotoUploadForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def home_view(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the valid photo here (e.g., save or further processing)
            return redirect('home_view')
    else:
        form = PhotoUploadForm()
    return render(request, 'home/home.html', {'form': form})

def about_view(request):
    return render(request, 'home/about.html')

def education_view(request):
    return render(request, 'home/education.html')

def experience_view(request):
    return render(request, 'home/experience.html')

def project_view(request):
    return render(request, 'home/project.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"📬 You got a new message from {name} <{email}>:\n\n{message}"

        send_mail(
            subject=f"New Contact Message from {name}",
            message=full_message,
            from_email=email,
            recipient_list=['your.email@gmail.com'],  # Your receiving email
            fail_silently=False,
        )

        messages.success(request, 'Thanks! Your message has been sent.')
        return redirect('contact')
    
    return render(request, 'home/contact.html')

def skill_view(request):
    return render(request, 'home/skill.html')

