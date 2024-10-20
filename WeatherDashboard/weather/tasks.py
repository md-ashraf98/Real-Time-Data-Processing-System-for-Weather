from celery_app import shared_task
import requests

@shared_task
def fetch_weather_data(city):
    """Fetches weather data for a specified city."""
    # Replace with your actual API key and endpoint
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(base_url)
        data = response.json()

        if response.status_code == 200:
            # Example of extracting some data
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            return {
                "city": city,
                "description": weather_description,
                "temperature": temperature
            }
        else:
            return {"error": data.get("message", "Failed to fetch weather data.")}

    except Exception as e:
        return {"error": str(e)}
