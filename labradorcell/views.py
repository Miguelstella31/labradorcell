# labradorcell/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world!")
