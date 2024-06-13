from langchain_helper import get_few_shot_db_chain
import streamlit as st

st.title("T shirt Inventory Management System : Q&A")

question = st.text_input("Enter your question here:")
if question:
    chain = get_few_shot_db_chain()
    answer = chain.run(question)
    st.header("Answer: ")
    st.write(answer)
