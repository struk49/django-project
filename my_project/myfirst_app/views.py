from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insert_content' : "Hello from myfirst_app"}
    return render(request, "myfirst_app/index.html", context=my_dict)
