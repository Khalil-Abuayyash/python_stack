from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db import models
import re
from django.db.models.deletion import CASCADE
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

class BookManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['desc']) < 5 :
            errors['desc'] = 'Description must be at least of five characters'

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255, default="") 
    last_name = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=255, default="")
    password = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManger()

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    likers = models.ManyToManyField(User, related_name="fav_books")
    uploader = models.ForeignKey(User, related_name="uploaded_books", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

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

def get_all_books():
    return Book.objects.all()

def get_fav_books(email):
    user = User.objects.get(email=email)
    fav_books = user.fav_books.all()
    return fav_books

def create_book(postData, email):
    title = postData['title']
    desc = postData['desc']
    user = User.objects.get(email=email)
    book = Book.objects.create(title=title, desc=desc, uploader=user)
    user.fav_books.add(book)
    return book.id

def get_book_details(book_id):
    book = Book.objects.get(id=book_id)
    return book

def favorite_book(user_id, book_id):
    user = User.objects.get(id=user_id)
    book = Book.objects.get(id=book_id)
    user.fav_books.add(book)

def edit_book(book_id, postData):
    book = Book.objects.get(id=book_id)
    book.title = postData['title']
    book.desc = postData['desc']
    book.save()


def delete_book(book_id):
    book = Book.objects.get(id=book_id)
    book.delete()