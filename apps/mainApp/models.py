from __future__ import unicode_literals
from django.db import models
from datetime import datetime

import re

now = str(datetime.now())

EMAILREGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9_.+-]+.[a-zA-Z]+$')

# Create your models here.

#<<------------------------USER MANAGER CLASS------------------------>>
#Create User Manager to Handle Validations
class UserManager(models.Manager):

    #PERFORM REGISTRATION VALIDATIONS
    def registration_validator(self, postData):

        print("POSTDATA is", postData)

        errors = {}

        #Name Validation
        if len(postData["name"]) < 1:
            errors["name"] = "Name is required"

        #Username Validation
        if len(postData["username"]) < 1:
            errors["username"] = "username is required"
        elif User.objects.filter(username = postData["username"]):
            errors["username"] = "Great one, but it's already taken!"

        #Password Validation
        if len(postData['password']) < 1:
            errors['password'] = "password is required"
        elif len(postData['password']) < 8:
            errors['password'] = "password must be 8 characters or longer!"
        if postData['confirm_password'] != postData['password']:
            errors['password'] = "Hey, these passwords don't match!!"
        return errors

    #PERFORM LOGIN VALIDATIONS
    def login_validator(self, postData):

        print("POSTDATA is", postData)

        errors = {}

        #Username Validation
        if len(postData["username"]) < 1:
            errors["username"] = "username is required"
        elif not User.objects.filter(username = postData["username"]):
            errors["username"] = "There is no username associated with this account!"

        #Password Validation
        if len(postData['password']) < 1:
            errors['password'] = "password is required"
        return errors


#<<------------------------ITEM MANAGER CLASS------------------------>>
class ItemManager(models.Manager):

    def item_validator(self, postData):
        errors = {}

        #Item Name Validation
        if len(postData["name"]) < 1:
            errors['name'] = "Please enter an item name."
        elif len(postData["name"]) < 3:
            errors['name'] = "Your destination must be 3 characters or longer."

        #Item Description Validation
        
        if len(postData["desc"]) < 1:
            errors['desc'] = "Please enter a description."
        elif len(postData["desc"]) < 10:
            errors['desc'] = "Your description must be 10 characters or longer."
        
        
        
        return errors

#<<------------------------USER CLASS------------------------>>
class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

    #represent method
    def __repr__(self):
        return f"User: {self.id} {self.name}"


#<<------------------------ITEM CLASS------------------------>>
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    #ONE TO MANY RELATIONSHIP
    added_by = models.ForeignKey(User, related_name="items", on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = ItemManager()


#MANY TO MANY RELATIONSHIP
class Favorite(models.Model):
    user = models.ForeignKey(User, related_name="user_favorites", on_delete = models.CASCADE)
    item = models.ForeignKey(Item, related_name="item_favorites", on_delete = models.CASCADE)



