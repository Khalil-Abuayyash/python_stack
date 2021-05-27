from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_shows),
    path('new', views.add),
    path('create', views.create_show),
    path('<int:id>', views.single_show),
    path('<int:id>/edit', views.edit),
    path('<int:id>/update', views.update),
    path('<int:id>/delete', views.delete)
]