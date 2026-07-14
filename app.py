import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

# Load API key
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Page configuration
st.set_page_config(
    page_title="AI FAQ Generator",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 AI FAQ Generator")
st.write("Generate Frequently Asked Questions (FAQs) using Generative AI.")

# Sidebar
with st.sidebar:
    st.header("⚙ Settings")

    topic = st.text_input(
        "Enter Topic",
        "Python Programming"
    )

    difficulty = st.selectbox(
        "Difficulty",
        ["Beginner", "Intermediate", "Advanced"]
    )

    number = st.slider(
        "Number of FAQs",
        1,
        10,
        5
    )

# Generate button
if st.button("🚀 Generate FAQs"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
        st.stop()

    prompt = f"""
Generate {number} Frequently Asked Questions on the topic "{topic}".

Difficulty Level: {difficulty}

For each FAQ provide:

Question:
Answer:

Return the output in a clear and readable format.
"""

    with st.spinner("Generating FAQs..."):

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
            max_tokens=1000
        )

        result = response.choices[0].message.content

    st.success("FAQs Generated Successfully!")

    st.subheader("Generated FAQs")

    st.write(result)

    st.download_button(
        label="📥 Download FAQs",
        data=result,
        file_name="FAQs.txt",
        mime="text/plain"
    )