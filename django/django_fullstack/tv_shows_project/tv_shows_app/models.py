from typing import NewType
from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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