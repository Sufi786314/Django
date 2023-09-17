#View created by admin Shaiban
from django.http import HttpResponse
from django.shortcuts import render
from myindustryapp.models import Contact
def index(request):
    return render(request,'index.html')
def updates(request):
    return render(request,'updates.html')
def contact(request):
    if request.method == "POST":
        print("THis is Post")
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        contact = Contact(name=name,email=email,phone=phone)
        contact.save()
    return render(request,"contact.html")