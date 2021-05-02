from django.shortcuts import render
from django.http import HttpResponse
import requests  

def index(request): 
    city = 'Sonipat'   
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c5998eec66c9a2c6393237712b4cdc0d'.format(city)
    r = requests.get(url).json()

    city_weather = {
       'city' :city,
       'temp' :r['main']['temp'],
       'description' :r['weather'][0]['description'],
       'icon' :r['weather'][0]['icon'],
    }
    context = {'cityweather':city_weather}

    return render(request, 'home.html', context )

    
