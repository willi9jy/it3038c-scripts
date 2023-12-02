Project 3: These set of python scripts provides you with your current weather and national news displayed as an html file. 

Requirements: Please install schedule, OpenWeatherMap, and ensure requests are installed as well.

Code:

pip install schedule
pip install OpenWeatherMap
pip install requests

Navigate to openweathermap.org, create an account, and once signed up, go to your account settings to copy your API code. 

Open the Project 3 folder open the WeatherAPI.py with a code editor(I used IDLE Shell because it is user friendly to me) and follow the configuration instructions in the script:
Run the command to ensure it works: open the command line, navigate to the file location, and run .\WeatherAPI.py. It will generate an html file(weather_report.html) with your 
current weather along with icon of the curret weather conditions.


Navigate to openweathermap.org, create an account, and once signed up, go to your account settings to copy your API code. 

Open the Project 3 folder open the NewsAPI.py with a code editor(I used IDLE Shell because it is user friendly to me) and follow the configuration instructions in the script:
Run the command to ensure it works: open the command line, navigate to the file location, and run .\NewsAPI.py. It will generate an html file(local_news.html) with your 
current weather along with icon of the curret weather conditions.
To set it up to run automatically upon login(optional):

Optional: Configuring the scheduler script

I've created a script that can auto-run these scripts at a desired time. Follow the instructions in the scheduler2.py file to configure the auto-run times/settings.

-------------------------

Sources:
openweathermap
NewsAPI
https://www.geeksforgeeks.org/python-schedule-library/
Previous labs.
