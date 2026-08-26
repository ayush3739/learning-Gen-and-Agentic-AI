from opcode import stack_effect
from typing import Annotated,Optional,Literal

from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages
from sympy import content
from torch import mode
from typing_extensions import TypedDict
from langchain.chat_models import init_chat_model
from openai import OpenAI
from dotenv import load_dotenv
import os 

load_dotenv('./.env')

client=OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.getenv("GITHUB_TOKEN"),
)


class State(TypedDict):
    user_query : str
    llm_output: Optional[str]
    is_good: Optional[bool]

def chat_bot(state: State):
    print("Chatbot Node", state)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user","content": state.get("user_query")}
        ]
    )
    state["llm_output"] = response.choices[0].message.content
    return state


def evaluate_response(state: State) -> Literal["chatbot_gemini", "endnode"]:
    print("evaluate Node", state)

    if False:
        return "endnode"
    
    return "chatbot_gemini"
    
def chatbot_gemini(state: State):
    print("Chatbot_gemini Node", state)
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "user","content": state.get("user_query")}
        ]
    )
    state["llm_output"] = response.choices[0].message.content
    return state

def endnode(state:State):
    print("end Node", state)

    return state

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot",chat_bot)
graph_builder.add_node("chatbot_gemini",chatbot_gemini)
graph_builder.add_node("endnode",endnode)

graph_builder.add_edge(START,"chatbot")
graph_builder.add_conditional_edges("chatbot",evaluate_response)

graph_builder.add_edge("chatbot_gemini","endnode")
graph_builder.add_edge("endnode",END)


graph = graph_builder.compile()

updated_state = graph.invoke(State({"user_query":"Hey,what is 2+2?"}))
print("Updated_State:",updated_state)