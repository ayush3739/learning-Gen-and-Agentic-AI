from typing_extensions import TypedDict,Annotated
from langgraph.graph import StateGraph,START,END
from openai import OpenAI
from typing import Optional,Literal
from dotenv import load_dotenv
import os 

load_dotenv('./.env')

client=OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.getenv("GITHUB_TOKEN"),
)

class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]

def chatbot(state: State):
    print("Chatbot state: ",state)
    response= client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role":"user","content": state.get("user_query")}
        ]
    )

    state["llm_output"]=response.choices[0].message.content
    return state

def evaluate_response(state: State) -> Literal["chatbot_gemini", "endnode"]:
    print("Evaluating response: ",state)
    llm_output= state.get("llm_output")
    
    if len(llm_output) < 20:  # too short, try gemini
        return "chatbot_gemini"
    return END

def chatbot_gemini(state: State):
    print("Chatbot Gemini state: ",state)
    enriched_query = f"{state.get('user_query')}\n\nPlease provide a detailed and elaborate answer."
    response= client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"user","content": enriched_query}
        ]
    )

    state["llm_output"]=response.choices[0].message.content
    return state

def endnode(state: State):
   print("End node reached with state: ",state)
   return state


graph_builder=StateGraph(State)

graph_builder.add_node("chatbot",chatbot)
graph_builder.add_node("evaluate_response",evaluate_response)
graph_builder.add_node("chatbot_gemini",chatbot_gemini)
graph_builder.add_node("endnode",endnode)

graph_builder.add_edge(START,"chatbot")
graph_builder.add_conditional_edges("chatbot", evaluate_response, {"chatbot_gemini": "chatbot_gemini", END: END})

graph_builder.add_edge("chatbot_gemini","endnode")
graph_builder.add_edge("endnode",END)

graph=graph_builder.compile()

updated_state=graph.invoke(State({"user_query":"what is 2+2? "}))
print("\n\nUpdated state after invoking the graph: ",updated_state)