from django.utils import timezone  # Correct import for timezone handling in Django
import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import WeatherData, WeatherAlert

API_KEY = '313df2b03ff34dc2d274ceed8a9fb676'
API_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
INDIAN_CAPITALS = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad',
                   'Lucknow', 'Jaipur', 'Bhopal', 'Patna', 'Chandigarh', 'Ranchi',
                   'Raipur', 'Bhubaneswar', 'Panaji', 'Gandhinagar', 'Thiruvananthapuram',
                   'Imphal', 'Shillong', 'Aizawl', 'Kohima', 'Agartala', 'Gangtok',
                   'Itanagar', 'Dispur', 'Shimla', 'Dehradun', 'Puducherry', 'Port Blair']


def index(request):
    return render(request, 'weather/index.html', {'indian_capitals': INDIAN_CAPITALS})


def fetch_weather_for_city(request):
    if request.method == 'GET':
        city = request.GET.get('city')

        api_key = '313df2b03ff34dc2d274ceed8a9fb676'
        weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        response = requests.get(weather_url)
        data = response.json()

        print("API Response:", data)  # Debugging: Check if the API returns data

        if response.status_code == 200:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'condition': data['weather'][0]['description'],
            }
            return JsonResponse(weather_data)
        else:
            return JsonResponse({'error': 'City not found!'}, status=404)


def fetch_weather_alerts(request):
    alerts = WeatherAlert.objects.all()
    alert_data = [
        {'city': alert.city, 'condition': alert.condition, 'alert_type': alert.alert_type, 'timestamp': alert.timestamp}
        for alert in alerts]
    return JsonResponse(alert_data, safe=False)