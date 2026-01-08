from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
if os.path.exists(".env"):
    load_dotenv(".env")
else:
    os.getenv("GROQ_API_KEY")==st.secrets["GROQ_API_KEY"]

groq_api_key=os.getenv("GROQ_API_KEY")

model=ChatGroq(model_name="llama-3.1-8b-instant", temperature=0.5, api_key=groq_api_key)
parser=StrOutputParser()

def get_length_range(length):
    if length == "Short":
        return "around 5 to 10 lines"
    elif length == "Medium":
        return "around 10-15 lines"
    elif length == "Long":
        return "around 15-20 lines"
    elif length == "Very Long":
        return "more than 20 lines"
    

def get_blog_post(topic,tone,length="Short"):
    length_line=get_length_range(length)
    prompt=PromptTemplate(
    template=""""
    You are an expert AI content writer and SEO strategist.

    Write a high-quality, well-structured, and engaging blog article on the topic: {topic}
    of length {length_line}.
    The tone of the blog should be {tone}.
""",
    input_variables=["topic","tone"],
    )
    chain=prompt | model | parser
    result=chain.invoke({"topic":topic,"tone":tone,"length_line":length_line})
    return result





    
