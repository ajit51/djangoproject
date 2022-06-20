from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request):
    date = datetime.datetime.now()
    print("test function is called from views")
    #return HttpResponse("<h1> Hello this is index page </h1>" +str(date))
    return render(request, "home.html", {})

def about(request):
    #return HttpResponse("<h1> Hello this is about page </h1>")
    return render(request, "about.html", {})

def service(request):
   return render(request, "services.html", {})