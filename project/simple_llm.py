import os
from langchain_community.llms import Cohere
#from langchain.chat_models import ChatOpenAI
import gradio as gr
from dotenv import load_dotenv
from langchain.llms import OpenAI
load_dotenv()

# with openai
# # assign API key
openai_api_key = os.getenv("OPENAI_API_KEY")


# gpt3 = OpenAI(model_name="text-ada-001" )

# with Huggingface
# from langchain import HuggingFaceHub


# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
# llm = HuggingFaceHub(repo_id="google/gemma-7b")
# text = "tell me insteresting fact about potato"


# with Cohere
cohere = Cohere(model='command-xlarge')

def chatbot(inpt):
    return cohere(inpt)

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")

demo.launch(server_name="0.0.0.0", server_port= 7860)