import datetime 
import socket 
import geocoder
import platform
import requests 

import tkinter as tk 

from tkinter import messagebox 

# Current date and time 

current_datetime = datetime.datetime.now()

formatted_time = current_datetime.strftime("%Y-%m-%d %I:%M %p")

# Hostname of the computer:

User = socket.gethostname() 

# Geo location(Appx.) based on IP
g = geocoder.ip('me')
city = g.city
state = g.state


# Weather API Call along with message pop-up
def get_current_weather(): 

    # Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap 

    API_KEY = 'PlaceAPIHere' 
    UNITS = 'IMPERIAL'
    CITY = 'Cincinnati'  # Replace with your city 

 

    # API endpoint for current weather by city name 

    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&units={UNITS}&appid={API_KEY}' 

 

    try: 

        response = requests.get(url) 

        weather_data = response.json() 

 

        # Extracting weather information 

        weather_description = weather_data['weather'][0]['description'] 

        temperature = weather_data['main']['temp'] 

        city_name = weather_data['name'] 

        humidity = weather_data['main']['humidity']

        wind_speed = weather_data['wind']['speed']



        message = f"Hello, {User}!\nThe current date & time is: {formatted_time}\nYour current is Location: {city}., {state}\nThe current weather in {city} is: {weather_description}, the temperature is: {temperature}°F, the humidity is: {humidity}%, the current wind Speed: {wind_speed} m/s."

        # Create a message box to display the weather information 

        messagebox.showinfo("Welcome back! ", message) 

    except requests.RequestException as e: 

        messagebox.showerror("Error", f"Failed to retrieve weather information: {e}") 

 

# Create a tkinter window 

root = tk.Tk() 

root.withdraw()  # Hide the root window 

 

# Call the function to get the current weather and display the message box 

get_current_weather() 

 

# Keep the window running 

root.mainloop() 
