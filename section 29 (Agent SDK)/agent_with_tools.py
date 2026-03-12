from agents import Agent, Runner, OpenAIChatCompletionsModel, function_tool
from bs4 import BeautifulSoup
import requests
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os,re

load_dotenv('./.env')

# Custom OpenAI client pointing to GitHub Models
client = AsyncOpenAI(
    api_key=os.getenv('GITHUB_TOKEN'),
    base_url="https://models.github.ai/inference",
)

@function_tool
def web_search_tool(website: str) -> str:
    """Fetches the content/title of a given website URL. Use this when the user asks about what's on a specific website.

    Args:
        website: The full URL of the website to fetch, e.g. https://blogpy.vercel.app
    """
    response = requests.get(website)
    soup= BeautifulSoup(response.text, 'html.parser')
    for tag in soup(['script', 'style', 'nav', 'footer', 'head']):
        tag.decompose()
    text = soup.get_text(separator=' ', strip=True)
    text = re.sub(r'\s+', ' ', text).strip() # remove extra whitespace and newlines
    return text if len(text) < 1000 else text[:1000] + "...(truncated)"

@function_tool
def get_weather(city: str) -> str:
    """Fetches current weather information for a given city.

    Args:
        city: The name of the city to get weather for, e.g. Greater Noida
    """
    city_encoded = city.replace(' ', '+')
    response = requests.get(f"https://wttr.in/{city_encoded}?format=j1", timeout=10)
    data = response.json()
    
    current = data['current_condition'][0]
    weather_desc = current['weatherDesc'][0]['value']
    temp_c = current['temp_C']
    feels_like = current['FeelsLikeC']
    humidity = current['humidity']
    wind_kmph = current['windspeedKmph']
    
    return (
        f"Weather in {city}: {weather_desc}\n"
        f"Temperature: {temp_c}°C (Feels like {feels_like}°C)\n"
        f"Humidity: {humidity}%\n"
        f"Wind Speed: {wind_kmph} km/h"
    )

# define an agent
agent = Agent(
    name='Hello world Agent',
    model=OpenAIChatCompletionsModel(
        model='openai/gpt-4o-mini',
        openai_client=client,
    ),
    instructions='''You are a fun and helpful assistant who responds with emojis and in a funny way. 🎉

        You have two tools available:
        - use get_weather when the user asks about weather for any city or location.
        - use web_search_tool when the user provides a website URL or asks about content on a specific website.

        Always call the appropriate tool to get real data — never make up weather or website content.
        Present the fetched information in a clear and fun way.
    ''',
    tools=[
        web_search_tool,
        get_weather,
    ]
)

result = Runner.run_sync(agent, "Hey can you please fetch weather information for Greater Noida ?")
print(result.final_output)