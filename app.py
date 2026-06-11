
from dotenv import load_dotenv 
load_dotenv() 

import streamlit as st 
import os 
import google.generativeai as genai 

if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
else:
    from dotenv import load_dotenv 
    load_dotenv() 
    api_key = os.getenv("GOOGLE_API_KEY")

# Configure the API key safely
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("API Key not found! Please check your Streamlit Secrets or .env file.")


model = genai.GenerativeModel("gemini-2.5-flash") 

def my_output(query):
    response = model.generate_content(query) 
    return response.text 

#### UI Development using streamlit 

st.set_page_config(page_title="SMART_BOT")
st.header("SMART_BOT") 
input = st.text_input("Input " , key = "input")  
submit = st.button("Ask your query") 

if submit :
    response = my_output(input) 
    st.subheader("The Response is-")
    st.write(response)



# question ----> LLM send ---> Response Textual Format 
