from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate
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

template = PromptTemplate(
    template= """Please summarize the research paper titled \"{paper_input}\" with the following specifications:\nExplanation Style: {style_input}  \nExplanation Length: {length_input}  \n1. Mathematical Details:  \n   - Include relevant mathematical equations if present in the paper.  \n   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  \n2. Analogies:  \n   - Use relatable analogies to simplify complex ideas.  \nIf certain information is not available in the paper, respond with: \"Insufficient information available\" instead of guessing.  \nEnsure the summary is clear, accurate, and aligned with the provided style and length.""",
    input_variables=["paper_input","style_input","lenght_input"]
)

prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
    })



if st.button('summrize'):
    result = model.invoke(prompt)
    st.write(result.content)







