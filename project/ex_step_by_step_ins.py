import gradio as gr
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()


from langchain import HuggingFaceHub

hugging_face_api = os.getenv("HUGGING_FACE_API_TOKEN")
os.environ["HUGGING_FACE_API_TOKEN"] = hugging_face_api
llm = HuggingFaceHub(repo_id="google/gemma-7b")


# # initialize the models
# openai = OpenAI(
#     model_name="gpt-3.5-turbo",
#     openai_api_key="YOUR API KEY"
# )

def chatbot(user_input):
    # defining a template
    template = """Question: {question}
    please provide step by step Answer:
    """
    prompt = PromptTemplate(template=template, input_variables=["question"])
    formated_prompt =prompt.format(question=str(user_input))
    return llm(formated_prompt)

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")

demo.launch()  