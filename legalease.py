import streamlit as st
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()   # Requires OPENAI_API_KEY in environment

# Function to get response from ChatGPT API
def get_chatgpt_response(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}],
        max_tokens=50
    )
    return response.choices[0].message["content"].strip()

# Dictionary of questions and answers
question_answer_pairs = {
    "What is your name?": "I am a chatbot.",
    "Hii": "Hii I am LegalEase.",
    "Hello": "Hi! How can I help you?",
    "What can you do?": "I can answer your questions and chat with you.",
    "i want some legal suggestion": "to resolve legal issue",
    "I can answer your questions and chat with you.",
    
    "I want to create a legal contract": """Creating a legally-binding contract involves several key steps:
1. Agreement
2. Identification of Parties
3. Definitions
4. Description of Services/Goods
5. Terms and Conditions
6. Consideration
7. Duration and Termination
8. Confidentiality
9. Governing Law
10. Signatures""",
    # ... keep all your dictionary items here ...
}

# UI
st.title("LegalEase")
st.header("Chat with LegalEase")

new_message = st.text_input("Enter your message:", "")

# Handle send button
if st.button("Send"):
    if new_message in question_answer_pairs:
        bot_response = question_answer_pairs[new_message]
    else:
        bot_response = get_chatgpt_response(new_message)

    st.text("⚖️ LegalEase: " + bot_response)
