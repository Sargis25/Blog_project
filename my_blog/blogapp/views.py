from django.shortcuts import render
from .forms import BlogApp
from .models import CommentBlog
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    if request.method == "POST":
        form = BlogApp(request.POST)
        if form.is_valid():
            form = BlogApp(request.POST)
            form.save()
            response = redirect('/thanks')
            return response
    else:
        form = BlogApp()
    return render(request, 'blogapp/index.html', {'form' : form})

def main(request):
    return render(request, 'blogapp/main.html')

def show(request):
    data = CommentBlog.objects.all()
    return render(request , 'blogapp/show.html', {'data' : data})

def thanks(request):
    return render(request, 'blogapp/thanks.html')






