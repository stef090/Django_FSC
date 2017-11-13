from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.
def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    context = {"help": "Help Page"}
    return render(request,"AppTwo/help.html",context=context)

def users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request,"AppTwo/users.html",context=context)
