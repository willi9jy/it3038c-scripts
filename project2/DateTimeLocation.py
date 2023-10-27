import datetime 

import socket 

import geocoder

import platform
import requests

# Current date and time 

current_datetime = datetime.datetime.now()

formatted_time = current_datetime.strftime("%Y-%m-%d %I:%M %p")

# Hostname of the computer:

User = socket.gethostname() 

# Geo location(Appx.) based on IP
g = geocoder.ip('me')
city = g.city
state = g.state

# Print the date, time, hostname and location 
print ("Hello,", User)
print("The current time is:", formatted_time)

print(f"Your current is Location: {city}, {state}")


#prints os info
os_info = platform.uname()
print(f"System: {os_info.system}")
print(f"Version: {os_info.version}")
print(f"Machine: {os_info.machine}")
print(f"Processor: {os_info.processor}")

# Prints current weather:
API_KEY = '04228c6317c9b53644ea2ef9a8ef785d'
CITY = 'Cincinnati'
UNITS = 'IMPERIAL'
url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&units={UNITS}&appid={API_KEY}'
response = requests.get(url) 

 

if response.status_code == 200: 

    data = response.json() 

    weather_description = data['weather'][0]['description'] 

    temperature = data['main']['temp'] 

    humidity = data['main']['humidity'] 

    wind_speed = data['wind']['speed'] 

 

    print(f'The current weather in {CITY}:') 

    print(f'Description: {weather_description}') 

    print(f'Temperature: {temperature}°C') 

    print(f'Humidity: {humidity}%') 

    print(f'Wind Speed: {wind_speed} m/s') 

else: 

    print(f'Error fetching weather data. Status code: {response.status_code}') 

