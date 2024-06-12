#Install package
# pip install google-generativeai
import os
import google.generativeai as genai
import streamlit as st
api_key='AIzaSyCcz5ZBpMBhX6fMFne7N1mDbB1ehKtqfV8'
genai.configure(api_key=api_key)
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)
st.title('Iam ChittiGPt')
st.subheader('Ask Me Anything You Want!!')
model=genai.GenerativeModel("gemini-pro")
Question=st.text_input("Ask me anything:")
submit=st.button("Enter")
if submit:
    response=model.generate_content(Question)
    print(st.write(response.text))