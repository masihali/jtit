from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'blog/index.html',{})
def login(request):
    return render(request, 'blog/login.html',{})
def posts(request):
    return render(request, 'blog/posts.html',{})
def post(request):
    return render(request, 'blog/post.html',{})
def add_education(request):
    return render(request, 'blog/add-education.html',{})
def add_experience(request):
    return render(request, 'blog/add-experience.html',{})

def create_profile(request):
    return render(request, 'blog/create-profile.html',{})

def dashboard(request):
    return render(request, 'blog/dashboard.html',{})
def profiles(request):
    return render(request, 'blog/profiles.html',{})
def profile(request):
    return render(request, 'blog/profile.html',{})
def register(request):
    return render(request,'blog/register.html',{})