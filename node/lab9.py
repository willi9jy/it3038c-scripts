import json 
import requests 
 

 
r = requests.get('http://localhost:3000') 
data = r.json() 
print("widget 1 is:", data[0]['color'])
print("widget 2 is:", data[1]['color'])
print("widget 3 is:", data[2]['color'])
