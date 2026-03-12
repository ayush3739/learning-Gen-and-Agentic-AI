from agents import Agent, Runner, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv('./.env')

# Custom OpenAI client pointing to GitHub Models
client = AsyncOpenAI(
    api_key=os.getenv('GITHUB_TOKEN'),
    base_url="https://models.github.ai/inference",
)

# define an agent
agent = Agent(
    name='Hello world Agent',
    model=OpenAIChatCompletionsModel(
        model='openai/gpt-4o-mini',
        openai_client=client,
    ),
    instructions='''You are an agent which greets the user and helps them ans using emojis and in funny way.''',
)

result = Runner.run_sync(agent, "Hey there , My name is Ayush Maurya ")
print(result.final_output)