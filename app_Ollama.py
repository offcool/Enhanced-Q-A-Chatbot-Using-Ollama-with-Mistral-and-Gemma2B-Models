import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama


import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Simple Q&A Chatbot With Ollama"

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful massistant . Please  repsonse to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,llm,temperature,max_tokens):
    llm=Ollama(model=llm)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

st.set_page_config(page_title="AI Chatbot", page_icon="favicon.png")


## #Title of the app
st.title("Enhanced Q&A chatbot with Ollama")


## Select the OpenAI model
llm=st.sidebar.selectbox("Select Open Source model",["gemma:2b","mistral"])

## Adjust response parameter
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## MAin interface for user input
st.write("Go ahead and ask any question")
user_input=st.text_input("You:")



if user_input :
    response=generate_response(user_input,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the user input")



st.markdown("---")
st.write("#### About this App")
# Link button with icon
st.link_button("For more information, visit us .","https://github.com/offcool/Enhanced-Q-A-Chatbot-Using-Ollama-with-Mistral-and-Gemma2B-Models") 

st.markdown("---")
st.markdown("© 2024 SHERPA Engineering MENA. All rights reserved.")






















