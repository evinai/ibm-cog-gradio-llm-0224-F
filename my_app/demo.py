# import os
# from langchain.llms import OpenAI
from langchain_community.llms import Cohere
#from langchain.chat_models import ChatOpenAI
import gradio as gr
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# # assign API key
# os.environ["OPENAI_API_KEY"] = "YOUR API KEY"
# os.environ["COHERE_API_KEY"] = os.getenv


# gpt3 = OpenAI(model_name="text-ada-001" )

cohere = Cohere(model='command-xlarge')

def chatbot(inpt):
    return cohere(inpt)

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")

demo.launch(server_name="0.0.0.0", server_port= 7860, share=True)