from django.shortcuts import render
import requests
# from datetime import datetime , timedelta
import datetime



# Create your views here.
def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Dhaka'
    
    appid = '75ff0ebd75db984e383798e74f7fe945'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid': appid, 'units': 'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    humidity = res['main']['humidity']
    speed = res['wind']['speed']
    day = datetime.date.today()
    time = res['timezone']
    # time = day + timedelta('timezone')
    # return render(request, 'weatherapp/index.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city})
    return render(request, 'index.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city, 'timezone': time, 'humidity': humidity , 'speed': speed})