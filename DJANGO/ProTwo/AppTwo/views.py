from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from AppTwo.models import User
from . import forms

# Create your views here.
def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    context = {"help": "Help Page"}
    return render(request,"AppTwo/help.html",context=context)

def users(request):
    # From Level Two
    # users = User.objects.all()
    # context = {'users': users}
    form=forms.UserForm()
    if request.method == "POST":
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("FORM INVALID!")


    return render(request,"AppTwo/users.html",{'form':form})
