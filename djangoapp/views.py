from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")


def home(request):
    return HttpResponse("This is my Root Page")

def host(request):
   # return HttpResponse("Host name of Django Server is %s" % request.get_host())	
    return HttpResponse("Welcome to the page at %s" % request.path)
#def current_datetime(request):
#    now = datetime.datetime.now()
#    html = "<html><body>It is now %s.</body></html>" % now
#    return HttpResponse(html)


#def current_datetime(request):
#    now = datetime.datetime.now()
#    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
#    html = t.render(Context({'current_date': now}))
#    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def pikka_name(request):
    name = "Parminderjit Benipal"
    t = get_template('pikka.html') 
    html = t.render(Context({'pikka_name': name}))
    return HttpResponse(html)			
