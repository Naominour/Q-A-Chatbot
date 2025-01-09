# Q&A Chatbot
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
import os 

# Load environment variables from .env file
load_dotenv()

# Function to load OpenAI model and get responses
def get_openai_response(question):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.6)
    response = llm.invoke(question)
    return response.content

# Initialize Streamlit
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

# Get user input
input = st.text_input("Ask your question:", key="input")
response = None

# Ask button
submit = st.button("Generate the Answer")

# If ask button is clicked, display the response
if submit and input:
    response = get_openai_response(input)
    st.subheader("The response is:")
    st.write(response)
