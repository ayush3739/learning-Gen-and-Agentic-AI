from openai import OpenAI
from dotenv import load_dotenv
import os,requests
import json


load_dotenv("./.env")

client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.getenv("GITHUB_TOKEN"),
)

def get_weather(city:str):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('OPENWEATHER_API_KEY')}&units=metric"
    response=requests.get(url)

    if response.status_code==200:
        return f"The weather in {city} is {response.text}"
    
    return "Something went Wrong"


available_tools={
    "get_weather":get_weather
}

system_Prompt="""
    You're an expert AI assistant named mikasa in resolving queries using chain of thought.
    You work on START ,PLAN and OUTPUT steps.
    you need to first PLAN what needs to be done. the PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    You can also call a tool if required from the list of available tool
    for every tool call wait for the observe step which is the output from the called  tool.

    Rules:
    - Strictly follow the JSON output format
    - Only run one step at a time.
    - The sequence of steps is START(where user gives an input), PLAN(that can be multiple
      steps) and OUTPUT (which is going to be displayed to the user).

    Output JSON Format:
    {"step":"START" | "PLAN" | "OUTPUT" | "TOOL" ,"content":"string","tool_name":"string","input":"string"}
    
    Available Tools:
    - get_weather: Takes city name as an input string and returns the weather info about the city 
    Example 1:
    START: Hey, can you Solve 2+3*5/10 
    PLAN: {"step":"PLAN","content": "Seems like user is interested in math problem"}
    PLAN: {"step":"PLAN","content": "looking at the problem, we should solve this using BODMAS method"}
    PLAN: {"step":"PLAN","content": "Yes, The BODMAS is correct thing to be done here"}
    PLAN: {"step":"PLAN","content": "first we must multiply 3 * 5 which is 15"}
    PLAN: {"step":"PLAN","content": "Now the new equation is 2 + 15 / 10"}
    PLAN: {"step":"PLAN","content": "Then we must divide 15 by 10 which is 1.5"}
    PLAN: {"step":"PLAN","content": "Now the new equation is 2 + 1.5"}
    PLAN: {"step":"PLAN","content": "Finally we must add 2 and 1.5 which is 3.5"}
    PLAN: {"step":"PLAN","content": "Great, we have solved and finnaly left with the answer 3.5 as answer"}
    OUTPUT: {"step":"OUTPUT","content": "3.5"}

    Example 1:
    START:  What is the weather of Delhi ?
    PLAN: {"step":"PLAN","content": "Seems like user is interested in weather information"}
    PLAN: {"step":"PLAN","content": "Let's see if we have a available tool to get the weather information from the available tools list"}
    PLAN: {"step":"PLAN","content": "I need to call the get_weather tool with Delhi as input"}
    TOOL: {"step":"TOOL","tool_name":"get_weather","input": "Delhi"}
    TOOL: {"step":"OBSERVE","tool_name":"get_weather","output": "The Temperature of delhi is clody with 20 C"}
    PLAN: {"step":"PLAN","content": "Great , I got the weather info about delhi ."}
    OUTPUT: {"step":"OUTPUT","content": "The Current weather of Delhi is cloudy with 20 degree celsius"}
"""

print("\n\n\n")

message_history=[
    {"role": "system", "content":system_Prompt},

]

user_query=input("👉⬜ ")
message_history.append({"role":"user","content":user_query})

while True: 
    response=client.chat.completions.create(
    model="openai/gpt-4o-mini",
    response_format={"type":"json_object"}, 
    messages=message_history
    )

    raw_result=response.choices[0].message.content
    message_history.append({"role":"assistant","content":raw_result})

    parsed_result=json.loads(raw_result)

    if parsed_result.get('step')=="START":
        print(f"🔥 : {parsed_result.get('content')}")
        continue

    if parsed_result.get('step')=="TOOL":
        tool_name=parsed_result.get('tool_name')
        tool_input=parsed_result.get('input')


        tool_response=available_tools[tool_name](tool_input)
        message_history.append({"role":"developer","content":json.dumps(
            {"step":"OBSERVE","tool_name":tool_name,"input":tool_input,"output":tool_response}
        )})
        print(f"🔧 : Calling tool {tool_name} with input {tool_input} ")

        continue
    

    if parsed_result.get('step')=="PLAN":
        print(f"🧠 : {parsed_result.get('content')}")
        continue
    if parsed_result.get('step')=="OUTPUT":
        print(f"✅ : {parsed_result.get('content')}")
        break

print("\n\n\n")




# print(get_weather("Delhi"))

# 👉⬜ Hello , Tell me the current weather of the paris , Goa, Shimla ?

#--------------------------------------
'''
🔥 : Hello , Tell me the current weather of the paris , Goa, Shimla ?
🧠 : User is asking for the current weather of three locations: Paris, Goa, and Shimla.        
🧠 : I will gather weather information for each location one by one, starting with Paris.      
🧠 : I will call the get_weather tool with 'Paris' as input.
🔧 : Calling tool get_weather with input Paris
🧠 : I have now retrieved the weather information for Goa. Next, I will get the weather for Shimla.
🔧 : Calling tool get_weather with input Shimla
🧠 : I have obtained the weather information for Shimla as well. Now I will summarize the weather data collected for all three locations.
✅ : The current weather information is as follows:
- Paris: The weather is misty with a temperature of 6.4°C, feels like 3.51°C. Humidity is 99%.
- Goa: The weather is clear with a temperature of 26.21°C, and humidity is 84%.
- Shimla: The weather is overcast with a temperature of 6.83°C, feels like 5.92°C. Humidity is 53%.


'''