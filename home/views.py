from django.shortcuts import render,HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    # return HttpResponse("This is my about Page")
    return render(request,'about.html')

def projects(request):
    # return HttpResponse("This is my projects Page")
    return render(request,'projects.html')
def contact(request):
    # return HttpResponse("This is my contact Page")
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        print(name, email, phone, desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("data has been written to db")
    return render(request,'contact.html')