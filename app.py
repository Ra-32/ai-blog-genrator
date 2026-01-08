import streamlit as st
from blog import get_blog_post,get_length_range
import time
st.title("AI Blog Genrator...✅⚡")

topic=st.sidebar.text_input("Enter the topic here...")


tone = st.sidebar.selectbox(
    "Select Blog Tone",
    [
        "Professional",
        "Conversational",
        "Beginner-friendly",
        "Technical",
        "Storytelling",
        "Persuasive",
        "Educational",
        "Startup / SaaS-focused",
        "Marketing-oriented",
        "Academic"
    ]
)

length=st.sidebar.selectbox(
    "Select Blog Length",
    [
        "Short",
        "Medium",
        "Long",
        "Very Long"
    ]
)


if st.sidebar.button("Generate Blog Post") and topic and tone and length:
    with st.spinner("Generating your blog... ✨"):
        time.sleep(3)  # simulate processing
        result = "Blog generated successfully!"
    length_line=get_length_range(length)
    blog_post=get_blog_post(topic,tone,length)

    st.write(blog_post)
    