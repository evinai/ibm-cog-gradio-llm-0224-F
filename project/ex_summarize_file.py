from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
# from langchain_community.llms import Cohere
import wget
import os
import gradio as gr
from dotenv import load_dotenv
load_dotenv()

# link to a text document
url = "https://raw.githubusercontent.com/hwchase17/chat-your-data/master/state_of_the_union.txt"
output_path = "state_of_the_union.txt"  # Local the file

# Check if the file already exists
if not os.path.exists(output_path):
    # Download the image using wget
    wget.download(url, out=output_path)

loader = TextLoader('state_of_the_union.txt')

## NEED OPENAI KEY

openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key


# Load the data loader
data = loader.load()

# Create the index instance that makes it searchable
index = VectorstoreIndexCreator().from_loaders([loader])

# Running into Gradio
def summarize(query):
    return index.query(query)

iface = gr.Interface(fn=summarize, inputs="text", outputs="text")
iface.launch(server_name="0.0.0.0", server_port= 7860)

## Q: when was independence declared?
## A: ->from gradio  The United States declared independence on July 4, 1776.