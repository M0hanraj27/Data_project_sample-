import streamlit as st
st.title('Welcome to D12 - Demo')
name = st.text_input('Enter your name:')
B = st.button("Submit")
if B:
    st.write(f"Hai {name}, welcome to D12 session")