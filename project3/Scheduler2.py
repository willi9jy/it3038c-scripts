import schedule 

import time 

import subprocess 

import os 

  

# Function to run a Python script 

def run_python_script(script_path): 

    try: 

        subprocess.run(["python", script_path], check=True) 

    except subprocess.CalledProcessError as e: 

        print(f"Error running script: {e}") 

  

# Function to open a file with the default associated application 

def open_file(file_path): 

    try: 

        os.startfile(file_path) 

    except OSError as e: 

        print(f"Error opening file: {e}") 

  

# Schedule the tasks. Put the path of each file in their correct spot

schedule.every().day.at("23:55").do(run_python_script, script_path=r"C:\Add\file\path\here.py") 
schedule.every().day.at("23:55").do(open_file, file_path=r"C:\Add\file\path\here.html") 
schedule.every().day.at("23:55").do(run_python_script, script_path=r"C:\Add\file\path\here.py") 
schedule.every().day.at("23:55").do(open_file, file_path=r"C:\Add\file\path\her.html")
  

# Keep the script running to allow scheduled tasks to execute 

while True: 

    schedule.run_pending() 

    time.sleep(1) 
