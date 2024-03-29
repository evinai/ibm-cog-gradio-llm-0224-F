import gradio as gr
from langchain.chains import LLMChain
from langchain.llms import Cohere
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
# setting up the LLM

#openai_api_key = os.getenv("OPENAI_API_KEY")
# os.environ["OPENAI_API_KEY"] = openai_api_key
# llm = OpenAI(temperature=0.9)

# from langchain_community.llms import HuggingFaceEndpoint

# Huggingface = os.getenv("HUGGING_FACE_API_TOKEN")
# os.environ["HUGGING_FAC_API_TOKEN"] = Huggingface
# llm = HuggingFaceEndpoint(repo_id="google/gemma-7b")

cohere = Cohere(model='command-xlarge')

def handle_complaint(complaint: str) -> str:
    #Create an instance of the LLM with a temperature value of 0.9 (higher values make the output more random).
    

    # Define the prompt template for the complaint handling
    prompt = PromptTemplate(input_variables=["complaint"], template="I am a customer service representative. I received the following complaint: {complaint}. My response is:")

    # Create a language model chain with the defined prompt template
    chain = LLMChain(llm=cohere, prompt=prompt)
    return chain.run(complaint)

# Create a Gradio interface for the handle_complaint function
iface = gr.Interface(fn=handle_complaint, inputs="text", outputs="text")
iface.launch()