from django.shortcuts import render
from django.http import HttpResponse
from myfirst_app.models import Topic, AccessRecord, Webpage, User

# Create your views here.
def index(request):
    return render(request, "myfirst_app/index.html")


def users(request):


    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, "myfirst_app/users.html", context=user_dict)
