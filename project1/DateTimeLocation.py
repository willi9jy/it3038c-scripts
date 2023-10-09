import datetime 

import socket 

import geocoder



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


