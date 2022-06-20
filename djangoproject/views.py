from django.http import HttpResponse
import datetime

def test(request):
    date = datetime.datetime.now()
    print("test function is called from views")
    return HttpResponse("<h1> Hello this is index page </h1>" +str(date))

def about(request):
    return HttpResponse("<h1> Hello this is about page </h1>")

def service(request):
    return HttpResponse("<h1> Hello this is service page </h1>")