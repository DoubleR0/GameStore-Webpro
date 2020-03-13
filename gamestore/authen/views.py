from builtins import object
from os.path import exists
from webbrowser import register
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


# Create your views here.
def logined(request):

    if request.method=="POST":
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        user = authenticate(request ,username=username, password=password)
        if user is not None:
            login(request, user)
            print("pass")
            return redirect('index')
        else:
            return render(request, template_name="authen/login.html", context={"fail":"Username or password was Wrong"})

    return render(request, template_name="authen/login.html", context={"fail":""})

def register(request):
    if request.method=="POST":
        firstname = request.POST.get("Firstname")
        lastname = request.POST.get("Lastname")
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        email = request.POST.get("Email")
        user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, password=password, email=email)
        user.set_password(password)
        user.save()
        return redirect("register")
    return render(request, template_name="authen/register.html")
