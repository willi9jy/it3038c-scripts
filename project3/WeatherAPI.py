import requests 

from datetime import datetime 

# Replace 'YOUR_API_KEY' with your OpenWeatherMap API key 

API_KEY = 'YOUR_API_KEY' 

CITY_NAME = 'cityyyy'  # Replace with the desired city name

UNITS = 'imperial'  # Use 'imperial' for Fahrenheit, 'metric' for Celsius 

  

# OpenWeatherMap API URL 

API_URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&units={UNITS}&appid={API_KEY}' 

  

# Fetch weather data 

response = requests.get(API_URL) 

data = response.json() 

  

# Extract relevant weather information 

temperature = data['main']['temp'] 

description = data['weather'][0]['description'] 

icon_code = data['weather'][0]['icon'] 

  

# Current date and time 

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 


# Create HTML content with CSS styling 

html_content = f""" 

<!DOCTYPE html> 

<html lang="en"> 

<head> 

    <meta charset="UTF-8"> 

    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 

    <style> 

        body {{ 

            font-family: Arial, sans-serif; 

            background-color: #fffffff; 

            text-align: center; 

        }} 

        .weather-container {{ 

            padding: 25px; 

            background-color: #e0dfe3; 

            border-radius: 10px; 

            box-shadow: 0 0 10px rgba(25, 20, 90, 0.1); 

            margin: 50px auto; 

            max-width: 400px; 

        }} 

        .temperature {{ 

            font-size: 2em; 

            font-weight: bold; 

        }} 

        .description {{ 

            margin-top: 10px; 

            color: #666; 

        }} 

        .icon {{ 

            width: 100px; 

            height: 100px; 

        }} 

        .timestamp {{ 

            margin-top: 20px; 

            color: #999; 

        }} 

    </style> 

    <title>Weather Report</title> 

</head> 

<body>


    <div class="weather-container"> 

        <div class="temperature">{temperature}F</div> 

        <div class="description">{description}</div> 

        <img class="icon" src="http://openweathermap.org/img/w/{icon_code}.png" alt="Weather Icon"> 

        <div class="timestamp">Updated at {current_time}</div> 

    </div> 

</body> 

</html> 

""" 

  

# Save HTML content to a file 

with open('weather_report.html', 'w') as html_file: 

    html_file.write(html_content) 

  

print("Weather report generated successfully. Check 'weather_report.html'.") 
