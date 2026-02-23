from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
llm = HuggingFaceEndpoint(
repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
task="text-generation")
model=ChatHuggingFace(llm=llm)

st.header=('Research Tool')

paper_input = st.selectbox("select the paperwork",["Attention is all you need","pre training og deep bidirectional transformers","GPT-3:Language models are few-short learners","Diffusion Modls Bear GANs on image synthesis"])

style_input = st.selectbox("select explanation style",["beginner friendly","Technical","Code Oriented","Mathematical"])

length_input=st.selectbox("select explanation length",["Beginner friendly","Technical","code-oreiented","Mathematical"])

#template

template= load_prompt('template.json')

prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
    })



if st.button('summrize'):
    result = model.invoke(prompt)
    st.write(result.content)







