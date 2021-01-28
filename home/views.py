from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact 
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        text=request.POST.get('text')
        contact=Contact(name=name,phone=phone,email=email,text=text,date=datetime.today())
        contact.save()
        messages.success(request, 'Your feedback has been sent!')
    return render(request,'contact.html')
    # return HttpResponse('This is contact page')