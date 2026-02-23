# 🧠 AI Prompt UI (LangChain + Streamlit)

This project is a simple AI chat application built using LangChain and HuggingFace models, with a Streamlit UI.

## 🚀 Features

- Dynamic prompt templates using LangChain
- Chat-based interface using Streamlit
- HuggingFace LLM integration
- Clean modular structure

## 🛠 Tech Stack

- Python 3.11
- LangChain
- HuggingFace
- Streamlit
- dotenv

## 📂 Project Structure

LCmodel/
│
├── app.py
├── ChatModels/
├── prompts/
├── requirements.txt
├── .gitignore

## ⚙️ Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/tharun790/prompt_ui.git
cd prompt_ui
```
2.Create virtual environment:
python -m venv .venv
source .venv/bin/activate   # Mac/Linux

3. Install dependencies:
pip install -r requirements.txt

4. Add your .env file:
   HUGGINGFACEHUB_API_TOKEN=your_token_here

5.Run the application:
streamlit run app.py
