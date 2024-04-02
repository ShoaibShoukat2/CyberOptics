from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.
def index(request):
    return render(request, 'basic/index.html')

def about(request):
    return render(request, 'basic/about.html')

def services(request):
    return render(request, 'basic/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        return render(request, 'basic/success.html')  # Redirect to a success page
    return render(request, 'basic/contact.html')

def terms(request):
    return render(request, 'basic/terms.html')



