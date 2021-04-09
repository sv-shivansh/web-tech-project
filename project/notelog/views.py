from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from .models import toDo 
from django.views.decorators.http import require_GET, require_POST

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        todos = toDo.objects.all().filter(user = request.user)
        return render(request, 'home.html', {'todos': todos})
    else:
        return render(request, 'landing.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check for errors
        if not username.isalnum():
            messages.error(
                request, "Username must be only letters and numbers.")
            return redirect('register')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if len(password1) < 6:
            messages.error(request, "Password should be greater than 6.")
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Already Registered. Try logging in")
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Already Registered. Try logging in")
            return redirect('register')

        # Create the user
        myuser = User.objects.create_user(username, email, password1)
        myuser.save()
        messages.success(request, "Successfully, Registered.")
        return redirect('login')
    return render(request, 'register.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully, Logged In.")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please try again.")
            return redirect('login')
    return render(request, 'login.html')

@csrf_exempt
def logout(request):
    logout(request)
    messages.success(request, "Successfully, Logged Out.")
    return redirect('home')

@require_POST
def addTodo(request):

    if request.method == 'POST':
        todos = toDo.objects.all().filter(user=request.user)
        user = request.user
        task = request.POST["task"]
        addmsg = toDo(task=task, user=user)
        addmsg.save()
        todos = toDo.objects.all().filter(user = request.user)
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')

def deletecomplete(request):
    toDo.objects.filter(user=request.user,isCompleted__exact=True).delete()
    return redirect('home')

def deleteAll(request):
    toDo.objects.filter(user=request.user).delete()
    return redirect('home')

def markasComplete(request):
    return redirect('home')