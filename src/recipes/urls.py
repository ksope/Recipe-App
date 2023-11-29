from django.urls import path
from .views import home

#specify the app name
app_name = 'recipes'

#URL configuration which maps a route with it's corresponding view
urlpatterns = [
   path('', home),
]