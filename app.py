import streamlit as st
from core.router import chat_pipeline

st.set_page_config(page_title="RAG Chat")

st.title("AI Knowledge Chat")

model = st.sidebar.selectbox(
    "Choose Model",
    ["gpt-4o-mini", "gpt-3.5-turbo"]
)

if "history" not in st.session_state:
    st.session_state.history = []

query = st.chat_input("Ask a question")

if query:
    st.chat_message("user").write(query)

    result = chat_pipeline(query, st.session_state.history, model)

    st.chat_message("assistant").write(result["answer"])

    st.session_state.history.append(
        {"role": "user", "content": query}
    )
    st.session_state.history.append(
        {"role": "assistant", "content": result["answer"]}
    )
