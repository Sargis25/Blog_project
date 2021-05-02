from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def register(request):
    if request.method == "POST":
        register = RegisterForm(request.POST)
        if register.is_valid():
            register = RegisterForm(request.POST)
            register.save()
            return redirect("/")
        else:
            return redirect("/")
    else:
        register = RegisterForm()

    return render(request, "register/register.html", {"register":register})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('mypage')
            else:
                return redirect('wrong')
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'register/login.html', {})

def mypage(request):
    return render(request, 'register/mypage.html')

def wrong(request):
    return(request, 'register/wrong.html')