from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from datetime import date, datetime
import re

class LoginValidation(models.Manager):
#remember to look into what is suppose to come after self,
    def login_validator(self, form):
        errors = {}
        # VALIDATES EMAIL
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(form['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
#!!!!WHEN SHOULD A DOUBLE TICK OR SINGLE TICK BE USED IN THE ERRORS[]!!!
        if len(form['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 3 characters"
#PASSWORD
        if len(form['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
# PASSWORD CONFIRMATION LOOKING FOR MATCH
        if form['password'] != form['pw_confirm']:
            errors['pw_confirm'] = "Password for account does not match"
# CHECK TO SEE IF EMAIL IN CORRECT FORMAT
        if not EMAIL_REGEX.match(form['email']):
            errors['regex'] = "Incorrect email format!"
        users_with_same_email = User.objects.filter(email=form['email'])
        if len(users_with_same_email) > 0:
            errors['duplicate'] = "Email already taken, try another one"            
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = LoginValidation()



class WishManager(models.Manager):
    def wish_validator(self, form):
        errors = {}
        if len(form['item']) < 3:
            errors["item"] = "A wish must have 3 characters"
        if len(form['description']) < 1:
            errors['description'] = "A description must be provided"
        return errors

class Wish(models.Model):
    item = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.ForeignKey(User, related_name='wishes', on_delete=models.CASCADE)
    granted = models.BooleanField(default=False)
    ## do not focus on many many; could be empty; do not need it for red belt; make sure I have the foreign key
    ###user.wishes
    user_likes = models.ManyToManyField(User, related_name='liked_posts')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = WishManager()