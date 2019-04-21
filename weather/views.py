import requests

from django.shortcuts import render


# Create your views here.


def weather(request):
    """
    Get weather of OpenWeatherMap API
    """
    # import geocoder
    # Weather through coordinates
    # g = geocoder.ip('me')
    # coord = g.latlng
    # url = "http://api.openweathermap.org/data/2.5/" \
    #     "weather?lat={}&lon={}&units=metric&lang=es" \
    #     "&appid=6c8ebfd3b99b04c856d28e97bab663c0". \
    #     format(coord[0], coord[1])

    # Weather through user's city
    userprofile = request.user.userprofile
    city = userprofile.city + ',es'
    if city == 'Álava,es':
        city = 'Principado de Asturias, es'
    url_city = "http://api.openweathermap.org/data/2.5/weather?q={}" \
        "&units=metric&lang=es&appid=6c8ebfd3b99b04c856d28e97bab663c0". \
        format(city)

    # Weather forecast
    url_forecast = "http://api.openweathermap.org/data/2.5/forecast?q={}" \
        "&units=metric&lang=es&" \
        "appid=6c8ebfd3b99b04c856d28e97bab663c0". \
        format(city)

    res = requests.get(url_city)
    data = res.json()
    city = userprofile.city
    temp = str(round(data['main']['temp'])) + "°"
    weather = data['weather'][0]['description'].capitalize()
    icon = data['weather'][0]['icon']
    url_icon = "http://openweathermap.org/img/w/{}.png".format(icon)

    res_forecast = requests.get(url_forecast)
    data_forecast = res_forecast.json()
    weather_temperature, weather_date, weather_description, weather_icon = [], [], [], []

    for element in range(40):
        if "12:00" in data_forecast['list'][element]['dt_txt']:
            weather_temperature.append(
                str(round(
                    data_forecast['list'][element]['main']['temp'])) + "°")
            weather_date.append(
                data_forecast['list'][element]['dt_txt'].split(" ")[0])
            weather_description.append(
                data_forecast['list'][element]['weather'][0]['description'].capitalize())
            icon_forecast = (
                data_forecast['list'][element]['weather'][0]['icon'])
            url_icon_forecast = (
                "http://openweathermap.org/img/w/{}.png".format(icon_forecast))
            weather_icon.append(url_icon_forecast)

    return render(
        request, 'weather/weather.html',
        {'temp': temp, 'weather': weather, 'url_icon': url_icon,
            'city': city, 'weather_temperature': weather_temperature,
            'weather_date': weather_date,
            'weather_description': weather_description,
            'weather_icon': weather_icon})
