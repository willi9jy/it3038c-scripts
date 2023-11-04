import json 
import requests 
 

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=04228c6317c9b53644ea2ef9a8ef785dY' % zip) 
data = r.json() 
print(data['weather'][0]['description']) 
