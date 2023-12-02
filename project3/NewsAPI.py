import requests 

from datetime import datetime 

  

# Replace 'YOUR_API_KEY' with your actual NewsAPI key 

NEWS_API_KEY = 'YOUR_API_KEY'
 

NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines' 

COUNTRY = 'us'  # Replace with your country code, e.g., 'us' for United States 

  

def get_local_news(api_key, country): 

    params = { 

        'apiKey': api_key, 

        'country': country, 

    } 

  

    response = requests.get(NEWS_API_ENDPOINT, params=params) 

  

    if response.status_code == 200: 

        return response.json()['articles'] 

    else: 

        print(f"Error: Unable to fetch news. Status Code: {response.status_code}") 

        return None 

  

def generate_html(news_data): 

    html_content = """ 

    <!DOCTYPE html> 

    <html lang="en"> 

    <head> 

        <meta charset="UTF-8"> 

        <meta name="viewport" content="width=device-width, initial-scale=1.0"> 

        <style> 

            body { 

                font-family: Arial, sans-serif; 

                background-color: #fffffff; 

                padding: 20px; 

            } 

            h1 { 

                color: #333; 

            } 

            .news-item { 

                margin-bottom: 20px; 

                padding: 10px; 

                background-color: #e0dfe3; 

                border-radius: 5px; 

                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); 

            } 

            .news-title { 

                font-size: 1.2em; 

                color: #333; 

            } 

            .news-description { 

                color: #000; 

            } 

        </style> 

        <title>Local News</title> 

    </head> 

    <body> 

        <h1>Local News</h1> 

    """ 
    
  

    for article in news_data: 

        title = article['title'] 

        description = article['description'] 

        url = article['url'] 

  

        html_content += f""" 

        <div class="news-item"> 

            <h2 class="news-title"><a href="{url}" target="_blank">{title}</a></h2> 

            <p class="news-description">{description}</p> 

        </div> 

        """ 

  

    html_content += """ 

    </body> 

    </html> 

    """ 

  

    return html_content 

  

if __name__ == "__main__": 

    news_data = get_local_news(NEWS_API_KEY, COUNTRY) 

  

    if news_data: 

        html_content = generate_html(news_data) 

  

        with open('local_news.html', 'w', encoding='utf-8') as html_file: 

            html_file.write(html_content) 

  

        print("HTML file generated successfully.") 

    else: 

        print("Failed to fetch news.") 
