import requests
from django.shortcuts import render

def index(request):
    """Main view to fetch weather."""
    weather_data = {}
    if request.method == "POST":
        city = request.POST.get('city')
        api_key = "6359e0a6cbb4ad25fa902b49f39d5334"  
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url, timeout=10)  
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],  
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            weather_data = {'error': 'City not found'}

    return render(request, 'weather.html', {'weather': weather_data})
