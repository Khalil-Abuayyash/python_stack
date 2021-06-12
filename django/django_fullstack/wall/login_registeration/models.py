from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db import models
import re
import bcrypt

class UserManger(models.Manager):
    def validator_registeration(self, postData):
        errors  = {}

        try:
            user = self.get(email=postData['email'])
            errors['exsited_email'] = f"{postData['email']} is already registered"
        except:
            pass
        
        if len(postData['first_name']) < 2 :
            errors['first_name'] = 'First name must be at least of two characters'

        if len(postData['last_name']) < 2 :
            errors['last_name'] = 'Last name must be at least of two characters'
        
        if len(postData['password']) < 8:
            errors['password'] = 'password must be at least of eight characters'
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['invalid_email'] = 'invalid email address'
        
        if postData['password'] != postData['confirm_password']:
            errors['password'] = 'password and coonfirm password are not the same'

        return errors
    
    def validator_login(self, postData):
        errors = {}
        try:
            user = self.get(email=postData['email'])

            if bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                pass
            else:
                errors['failed_password'] = "email and password are not matched"

        except:
            errors['existed_email'] = f"{postData['email']} is not registered"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255, default="") 
    last_name = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=255, default="")
    password = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManger()

def create_user(postData):
    first_name = postData['first_name']
    last_name = postData['last_name']
    email = postData['email']
    password  = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode() 
    User.objects.create(first_name=first_name, last_name=last_name,email=email, password=password)
    return User.objects.last()

def get_user_details(email):
    user = User.objects.get(email=email)
    user_details = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        # 'created_at': user.created_at,
        # 'updated_at': user.updated_at,
    }

    return user_details

