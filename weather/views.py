from django.shortcuts import render
from django.http import request
import requests
from .models import Weather


def weather(request):

   
   
   
   if request.method=='POST':
      name=request.POST.get('name')
   else:
      name='Kolkata'

   api='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=3ef770c5bde684b66dbc2a7537492d9c'
   

   #city=Weather.objects.all()
   
   city=name
   
   

   
   
   city_weather = requests.get(api.format(city)).json()
   weather = {



       'city' : city,
       'temperature' : city_weather['main']['temp'],
       'description' : city_weather['weather'][0]['description'],
       'icon' : city_weather['weather'][0]['icon']
    }
   return render(request,'weather.html',{'weather':weather})
