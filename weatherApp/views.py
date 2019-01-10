import requests
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    url ='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c99a630bdb6897a61e035784ec774d76'
    city = 'Dhaka'
    r = requests.get(url.format(city)).json()
    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon'],

    }
    context = {
        'city_weather': city_weather
    }
    print(city_weather)
    return render(request,'index.html',context)