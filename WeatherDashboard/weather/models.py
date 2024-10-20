from django.db import models
from django.core.mail import send_mail
from django.conf import settings

class WeatherData(models.Model):
    city = models.CharField(max_length=255)
    temperature = models.FloatField()
    feels_like = models.FloatField()
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    condition = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

class WeatherAlert(models.Model):
    city = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    alert_type = models.CharField(max_length=255)
    email = models.EmailField()  # For alerts
    timestamp = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create_alert(cls, city, condition, alert_type, email):
        alert = cls.objects.create(city=city, condition=condition, alert_type=alert_type, email=email)
        send_mail(
            f'Weather Alert for {city}',
            f'Condition: {condition}, Alert Type: {alert_type}',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

