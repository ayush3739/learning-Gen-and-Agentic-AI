from typing_extensions import TypedDict,Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph,START,END
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os 

load_dotenv('./.env')

llm=init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai",
    base_url="https://models.github.ai/inference",
    api_key=os.getenv("GITHUB_TOKEN"),
)

class State(TypedDict):
    messages: Annotated[list, add_messages] # it adds messages to the state, and also allows us to use the messages in the graph 


def chatbot(state: State):
    response= llm.invoke(state.get("messages"))
    return {"messages": [response]} # it returns a dictionary with the key "messages" and the value is a list of messages, in this case it will return the response from the llm

def samplenode(state: State):
    print("\n\nInside sample node",state)
    return {"messages": ["Sample message appended to the state"]}

graph_builder=StateGraph(State) #graph builder for the state graph, it takes the state as a parameter
graph_builder.add_node("chatbot",chatbot) # adding the chatbot node to the graph builder, it takes the name of the node and the function that will be executed when the node is called
graph_builder.add_node("samplenode",samplenode) # adding the samplenode node to the graph builder, it takes the name of the node and the function that will be executed when the node is called



# (START) -> chatbot -> samplenode -> (END)

graph_builder.add_edge(START,"chatbot")
graph_builder.add_edge("chatbot","samplenode")
graph_builder.add_edge("samplenode",END)

graph= graph_builder.compile() # compiling the graph builder to create the graph, it will check for any errors in the graph and also create the graph structure

updated_state=graph.invoke(State({"messages":"Hi , MY name is Ayush Maurya"}))
print("\n\nUpdated state after invoking the graph: ",updated_state)

# state ={messages: ["Hey there "]} 
# node runs : chatbot(state: ["Hey there "]) -> ["Hi,  this is a message from ChaBot Node"]
# state= {messages: ["Hey there ", "Hi,  this is a message from ChaBot Node"]}
