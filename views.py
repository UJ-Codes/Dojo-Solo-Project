from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.db import models
from datetime import date, datetime
from django.contrib import messages
from .models import User
#from .models import Wish
import bcrypt
import re


def login_page(request):
#    context = {
#        'wishes': Wish.objects.all()
#    }
    return render(request, 'login.html')
    print('I am here')


def register(request):
    if request.method == "POST":
        print('I am registering now')
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/register')
            print('I am registered')
        else:
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            print(hashed_pw)
            user = User.objects.create(first_name=request.POST['first_name'], 
            last_name=request.POST['last_name'],
            email=request.POST['email'], 
            password=hashed_pw)
            request.session['user_id'] = user.id
            messages.success(request, "You have successfully registered!")     
            return redirect('/account')       
    return redirect('/login_page') 



def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if len(user) > 0:
#TAKE VALUE FROM THE LIST AND MAKE IT THE VALUE OF THE USER. instead of having a whole list
        user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
#            messages.success(request, "You have logged in successfully!")
            return redirect('/account')
#do not need else, code will folllow to this line
    messages.error(request, "Email or password is incorrect")
    return redirect('/login_page') 


def success(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to log in!")
        return redirect('/')
    context = {
#we can use get instead of filter because we know it is in database
        'user': User.objects.get(id=request.session['user_id']),
        'all_wishes': Wish.objects.all()
    }
    return render(request, 'account.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')


def about(request):
#    context = {
#        'wishes': Wish.objects.all()
#    }
    return render(request, 'about.html')
    print('I am here')


def account(request):
#    context = {
#        'wishes': Wish.objects.all()
#    }
    return render(request, 'account.html')
    print('I am here')



def schedule(request):
#    context = {
#        'wishes': Wish.objects.all()
#    }
    return render(request, 'schedule.html')
    print('I am here')

def update(request):
#    context = {
#        'wishes': Wish.objects.all()
#    }
    return render(request, 'update.html')
    print('I am here')


def work(request):
#    context = {
#        'wishes': Wish.objects.all()
#    }
    return render(request, 'work.html')
    print('I am here')


def location(request):
#    context = {
#        'wishes': Wish.objects.all()
#    }
    return render(request, 'location.html')
    print('I am here')

def review(request):
#    context = {
    #    'wish': wish_one
    # }
    return render(request, 'review.html')
    print('I am here')

def create_wish(request):
    errors = Wish.objects.wish_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    Wish.objects.create(item = request.POST['item'], description = request.POST['description'], poster = User.objects.get(id=request.session['user_id']))
###########
#    poster = User.objects.get(id=request.session['id'])
#    item = Wish.objects.get(id=id)
#    poster = User.objects.get(id=request.session['id'])
#    Wish.objects.create(item = request.POST['item'], description = request.POST['description'])
    #Wish.objects.create(item = request.POST['item'], poster=poster, description = request.POST['description'])
    return redirect('/review')