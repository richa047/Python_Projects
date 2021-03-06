#status- issue with pip not able to download pyowm
#https://www.youtube.com/watch?v=O9G4vBsiV40
import pyowm

owm = pyowm.OWM(
    '3d786607dc39303f2fccb3bf870428bc')

city = 'Lisbon'
loc = owm.weather_at_place(city)
weather = loc.get_weather()

# temperature
temp = weather.get_temperature(unit='celsius')

for key,val in temp.items():
    print(f'{key} => {val}')

# humidity, wind, rain, snow
humidity = weather.get_humidity()
wind = weather.get_wind()
rain = weather.get_rain()
snow = weather.get_snow()

print(f'humidity = {humidity}')
print(f'wind = {wind}')
print(f'rain = {rain}')
print(f'snow = {snow}')

# sun rise and sun set
sr = weather.get_sunrise_time(timeformat='iso')
ss = weather.get_sunset_time(timeformat='iso')
print(f'SunRise = {sr}') 
print(f'SunSet = {ss}')

# clouds and rain
loc = owm.three_hours_forecast(city)

clouds = str(loc.will_have_clouds())
rain = str(loc.will_have_rain())

print('will have clouds? ' + clouds)
print('will have rain? ' + rain)