from agents import Agent,Runner,OpenAIChatCompletionsModel
import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv('./.env')


client = AsyncOpenAI(
    api_key=os.getenv('GITHUB_TOKEN'),
    base_url="https://models.github.ai/inference",
)

japanese_agent=Agent(
    name='Japanese Agent',
    model=OpenAIChatCompletionsModel(
        model='openai/gpt-4o-mini',
        openai_client=client,
    ),    
    instructions="You translate the user's message to French",
)

german_agent=Agent(
    name='German Agent',
    model=OpenAIChatCompletionsModel(
        model='openai/gpt-4o-mini',
        openai_client=client,
    ),      
    instructions="You translate the user's message to German",
)


orchestrator_agent = Agent(
    name="orchestrator_agent",
    model=OpenAIChatCompletionsModel(
        model='openai/gpt-4o-mini',
        openai_client=client,
    ),      
    instructions=(
        "You are a translation agent. You use the tools given to you to translate."
        "If asked for multiple translations, you call the relevant tools."
    ),
    tools=[
        japanese_agent.as_tool(
            tool_name="translate_to_japanese",
            tool_description="Translate the user's message to Japanese",
        ),
        german_agent.as_tool(
            tool_name="translate_to_german",
            tool_description="Translate the user's message to German",
        ),
    ],
)

async def main():
    result = await Runner.run(orchestrator_agent, input="Say hello , how are you ? in japanese and german ")
    print(result.final_output)
    print(result.raw_responses)

asyncio.run(main())