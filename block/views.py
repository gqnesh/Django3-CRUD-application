from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from block import models
from django.contrib import messages
import re

# Create your views here.

def home(request):

    data = models.Post.objects.all()
    info = {'info': data}

    return render(request, 'block/home.html', info)

def dashboard(request):

    if request.user.is_authenticated:
        if request.user.id == 1:
            data = models.Post.objects.all()
            info = {'info': data}
            
            return render(request, 'block/dashboard.html', info)
        else:
            post = models.Post.objects.filter(user_id = request.user.id)
            info = {'info': post}
            return render(request, 'block/dashboard.html', info)
    else:
        return HttpResponseRedirect('/')
def addpost(request):

    if request.method == 'POST':

        title = request.POST['title']
        desc = request.POST['desc']

        print(title, desc)

        post = models.Post(title = title, desc = desc, user_id = request.user.id)
        post.save()
        return HttpResponseRedirect('/dashboard/')
        
    return render(request, 'block/addpost.html')

def editpost(request, id):

    post = models.Post.objects.filter(id = id)

    if request.method == 'POST':
        
        Etitle = request.POST['Etitle']
        Edesc = request.POST['Edesc']

        if request.user.is_authenticated:

            post = models.Post.objects.get(id = id)
            post.title = Etitle
            post.desc = Edesc
            post.save()

            return HttpResponseRedirect('/dashboard/')
    else:

        info = {'info': post}
        return render(request, 'block/editpost.html', info)

def deletepost(request, id):

    post = models.Post.objects.get(id=id)
    post.delete()

    return HttpResponseRedirect('/dashboard/')

def user_signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        passwd = request.POST['passwd']

        try:
            user = User.objects.get(username = uname)
            messages.error(request, 'Already username exist !')
            return render(request, 'block/user_signup.html')

        except:
            pass

        user = User.objects.create_user(username=uname, email=email, password=passwd)
        user.first_name = fname
        user.last_name = lname

        my_group = Group.objects.get(name = 'User')
        user.groups.add(my_group)
        
        user.save()

        return render(request,'block/user_signin.html')
    else:
        return render(request, 'block/user_signup.html')

def user_signin(request):
    if request.method == 'POST':
        username = request.POST['Suname']
        passwd = request.POST['Spasswd']

        user = authenticate(request, username=username, password=passwd)

        if user is not None:
            if user.is_authenticated:
                login(request, user)
                
                u = user.get_username()
                d1 = {'val': u}
                return render(request, 'block/home.html', d1)
            else:
                return HttpResponseRedirect('user_signin')
        else:
            return render(request, 'block/user_signin.html')
    else:
        return render(request, 'block/user_signin.html')

def forgotpassword(request):

    if request.method == 'POST':

        Funame = request.POST['Funame']
        Fpasswd = request.POST['Fpasswd']
        Fpasswd1 = request.POST['Fpasswd1']

        u = User.objects.get(username=Funame)
        if Fpasswd == Fpasswd1:
            u.set_password(Fpasswd1)
            u.save()
            return render(request, 'block/user_signin.html')

    return render(request, 'block/forgotpassword.html')

def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/')

def contact(request):
    return render(request, 'block/contact.html')

def about(request):
    return render(request, 'block/about.html')
