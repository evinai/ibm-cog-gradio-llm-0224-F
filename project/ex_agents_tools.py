import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain_community.llms import Cohere
# from langchain.llms import OpenAI 

# openai_api_key = "YOUR API KEY"
# os.environ["OPENAI_API_KEY"] = openai_api_key
# gpt3 = OpenAI(model_name='gpt-3.5-turbo')

# using cohere instead of openai
cohere = Cohere(model='command-xlarge')

# Equipting the agent with some tools
tools = load_tools([ "llm-math", "python_repl", "requests_all", "human"], llm=cohere)

# Defining the agent
agent = initialize_agent(tools, llm=cohere, agent="zero-shot-react-description", verbose=True)
agent.run("create simple matplotlib showing sin function and plot it")