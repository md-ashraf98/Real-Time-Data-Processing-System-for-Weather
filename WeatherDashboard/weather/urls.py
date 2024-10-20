from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weather/', views.fetch_weather_for_city, name='fetch_weather_for_city'),
]
