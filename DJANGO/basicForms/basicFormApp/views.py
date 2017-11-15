from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    return render(request,'basicFormApp/index.html')

def form_name_view(request):
    form=forms.BaseForm()
    if request.method == "POST":
        form = forms.BaseForm(request.POST)

        if form.is_valid():
            #DO SOMETHING CODE
            print("VALIDATED REQUEST!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])


    return render(request,'basicFormApp/form_page.html',{'form':form})
