from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
@login_required(login_url='signin')
def index(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'index.html')

def signup(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password==confirmpassword:
           if User.objects.filter(email=email).exists():
               messages.info(request, 'Email already taken')
               return redirect('signup')
           elif User.objects.filter(username=username).exists():
               messages.info(request, 'Username already taken')
               return redirect('signup')
           else:
               user=User.objects.create_user(username=username,email=email,password=password)
               user.save()
               user_login=auth.authenticate(username=username,password=password)
               auth.login(request,user_login)

               user_model=User.objects.get(username=username)
               new_profile=Profile.objects.create(user=user_model, id_user=user_model.id)
               new_profile.save()
               return  redirect('settings')
        else:
            messages.info(request, "Passwords do not match.Please confirm and try again")
            return redirect('signup')
    else:
        return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request,'Incorect username or password')
            return redirect('signin')

    else:
        return render(request,'signin.html')
@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def settings(request):
    user_profile= Profile.objects.get(user=request.user)
    if request.method=='POST':
        if request.FILES.get('picture')!=None:
            picture = request.FILES.get('picture')

        else:
            picture = user_profile.picture
        bio=request.POST['bio']
        location = request.POST['location']
        work = request.POST['work']
        relationship= request.POST['relationship']

        user_profile.picture=picture
        user_profile.location=location
        user_profile.bio=bio
        user_profile.work=work
        user_profile.relationship=relationship
        user_profile.save()
        return redirect('settings')

    return render(request,'setting.html',{'user_profile':user_profile})

@login_required(login_url='signin')
def upload(request):
    return HttpResponse('hello')