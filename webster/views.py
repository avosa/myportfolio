from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Contact
# Create your views here.


# Home/Index View
def index(request):
    # check post method and request type
    return render(request, 'webster/home.html')


#Portfolio View
def project(request):
    return render(request, 'webster/project.html')

# About View
def about(request):
    return render(request, 'webster/about.html')


# Contact View
def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        form = Contact(email=email, subject=subject, message=message)
        # Saving Form data to Database
        form.save()

        return render(request, 'webster/contact.html')
    else:
        return render(request, 'webster/contact.html')
