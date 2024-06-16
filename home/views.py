from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request):                            # Function to display the index.html file
    return render(request,'index.html')

def about(request):                            # Function to redirect user to about page
    return render(request,'index.html')

def student(request):                          # Function to redirect Student to Login page
    return render(request,"login.html")

def teacher(request):                          # Function to redirect Teacher to Login page
    return render(request,"login.html")

def contact(request):                          # Function to redirect user to contact page         
    return HttpResponse("contact us here aquibpc@gmail.com")


