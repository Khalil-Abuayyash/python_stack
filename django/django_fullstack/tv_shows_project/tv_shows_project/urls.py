from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('', lambda request : redirect('/shows')),
    path('shows/', include('tv_shows_app.urls'))
]
