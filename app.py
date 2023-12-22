from api import llm_output, get_and_init_llm


import streamlit as st

# ask for api key
key = st.text_input("Enter your API key")
if key:
    app = get_and_init_llm(key)

prompt = st.chat_input("Ask anything about Polygon ID!!")

if prompt:
    response = llm_output(prompt,app)
    st.write(f"User Question: {prompt}")
    st.write(f"Polygon AI: {response}")
