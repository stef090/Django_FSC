from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    context = {"help": "Help Page"}
    return render(request,"AppTwo/help.html",context=context)
