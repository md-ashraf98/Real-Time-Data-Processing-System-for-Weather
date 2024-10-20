from django.contrib import admin
from django.urls import path
from weather import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('weather/', views.fetch_weather_for_city, name='fetch_weather'),
    path('weather/alerts/', views.fetch_weather_alerts, name='fetch_weather_alerts'),
]
