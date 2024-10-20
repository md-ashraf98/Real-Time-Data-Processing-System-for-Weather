from django.core.management.base import BaseCommand
from weather.models import WeatherData, WeatherAlert
import requests
from django.utils import timezone

API_KEY = '313df2b03ff34dc2d274ceed8a9fb676'
API_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
INDIAN_CAPITALS = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad',
                   'Lucknow', 'Jaipur', 'Bhopal', 'Patna', 'Chandigarh', 'Ranchi',
                   'Raipur', 'Bhubaneswar', 'Panaji', 'Gandhinagar', 'Thiruvananthapuram',
                   'Imphal', 'Shillong', 'Aizawl', 'Kohima', 'Agartala', 'Gangtok',
                   'Itanagar', 'Dispur', 'Shimla', 'Dehradun', 'Puducherry', 'Port Blair']

class Command(BaseCommand):
    help = 'Fetch weather data from OpenWeather API'

    def handle(self, *args, **kwargs):
        for city in INDIAN_CAPITALS:
            response = requests.get(API_URL.format(city, API_KEY))
            if response.status_code == 200:
                data = response.json()
                temperature = data['main']['temp'] - 273.15
                feels_like = data['main']['feels_like'] - 273.15
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']
                weather_condition = data['weather'][0]['main']

                WeatherData.objects.update_or_create(
                    city=city,
                    defaults={
                        'temperature': temperature,
                        'feels_like': feels_like,
                        'humidity': humidity,
                        'wind_speed': wind_speed,
                        'condition': weather_condition,
                        'timestamp': timezone.now()
                    }
                )
