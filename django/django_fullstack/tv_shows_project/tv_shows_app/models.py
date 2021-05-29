from typing import NewType
from django.db import models
from datetime import date

class ShowManger(models.Manager):
    def validator(self, postData):
        today = date.today()
        today = {
            'day': today.day,
            'month': today.month,
            'year': today.year
        }

        errors = {}

        show = self.get(title=postData['title'])
        print('show')
        print(show)
        print(type(show))

        if show :
            errors['unique_title'] = f"{postData['title']} does exist"
        if len(postData['title']) < 2:
            errors['title'] = "Title must be at least of two characters"
        
        if len(postData['network']) < 3:
            errors['network'] = "Network must be at least of three characters"
        
        if len(postData['desc']) < 10 and len(postData['desc']) > 0:
            errors['desc'] = "Description is optional, but if exists then must be at least of ten characters"
        
        release_date =  postData['release_date'].split('-')
        release_date = list(map(int, release_date))

        if release_date[0] > today['year']:
            errors['release_date'] = "Release Date must be in the past"
        elif release_date[1] > today['month']:
            errors['release_date'] = "Release Date must be in the past"
        elif release_date[2] > today['day']:
            errors['release_date'] = "Release Date must be in the past"

        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManger()

def all_shows():
    return Show.objects.all()


def create(data):
    title = data['title']
    network = data['network']
    release_date = data['release_date']
    desc = data['desc']
    Show.objects.create(title = title, network = network, release_date = release_date, desc = desc)
    return Show.objects.last().id

def single_show(id):
    show = Show.objects.get(id=id)
    return {
        'id': show.id,
        'title': show.title,
        'network': show.network,
        'release_date': show.release_date,
        'desc': show.desc,
        'updated_at': show.updated_at
    }




def update(id, data):
    show = Show.objects.get(id=id)
    show.title = data['title']
    show.network = data['network']
    show.release_date = data['release_date']
    show.desc = data['desc']
    show.save()

    return {
        'id': show.id,
        'title': show.title,
        'network': show.network,
        'release_date': show.release_date,
        'desc': show.desc,
        'updated_at': show.updated_at
    }

def delete(id):
    Show.objects.get(id=id).delete()