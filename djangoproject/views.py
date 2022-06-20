from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request):
    date = datetime.datetime.now()
    print("test function is called from views")
    #return HttpResponse("<h1> Hello this is index page </h1>" +str(date))
    isActive = True
    name = "Ajit Kumar"
    list_of_programs = [
        "WAP to check even or odd",
        "WAP to check prime number",
        "WAP to print all prime number from 1 to 100",
        "WAP to print Pascal tringle"
    ]
    student = {
        "student_name" : "Rahul",
        "student_college" : "XYZ",
        "student_city" : "Mumbai"
    }

    data = {
            'date' : date,
            'isActive' : isActive,
            'name' : name,
            'list_of_programs' : list_of_programs,
            'student_data' : student
            }
    return render(request, "home.html", data)

def about(request):
    #return HttpResponse("<h1> Hello this is about page </h1>")
    return render(request, "about.html", {})

def service(request):
   return render(request, "services.html", {})