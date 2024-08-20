# Q&A Chatbot
In this project we develop a **Question & Answer (Q&A) chatbot** using **LangChain** and **Streamlit**. The chatbot uses OpenAI's gpt-3.5-turbo model to generate responses to user queries in real-time.

<img src="image\Result.png" style="width:1000px;">

![OpenAI](https://img.shields.io/badge/Skill-OpenAI-yellow)
![GPT](https://img.shields.io/badge/Skill-GPT-blueviolet)
![LangChain](https://img.shields.io/badge/Skill-LangChain-orange)
![Conversational Bot](https://img.shields.io/badge/Skill-Conversational%20Bot-green)


## Features

- **Real-time Q&A:** Ask questions and receive responses instantly using the gpt-3.5-turbo model.
- **Streamlit Interface:** A simple and interactive user interface for asking questions.
- **Customizable Temperature:** Adjust the creativity of the responses by modifying the temperature parameter.


## Installation
1. **Prerequisites**:
   - Python 3.8 or higher
   - OpenAI API Key

2. **Clone the Repository**:
```bash
git clone https://github.com/your-username/qa-chatbot.git
cd qa-chatbot
```
3. **Set Up Virtual Environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
4. **Install Dependencies**:
```bash
pip install -r requirements.txt
```
5. **Set Up Environment Variables**:
   - Create a .env file in the project root directory and add your OpenAI API key:
```bash
OPENAI_API_KEY=your-openai-api-key
```
6. **Running the Application**:
   - Run the Streamlit application using the following command:
```bash
streamlit run app.py
```
After running the command, Streamlit will start a local web server. You can access the Q&A chatbot by navigating to http://localhost:8501 in your web browser.


## Customization
- **Model:** The chatbot uses the `gpt-3.5-turbo` model by default. You can change the model by modifying the `model_name` parameter in the `ChatOpenAI` class. 
- **Temperature:** Adjust the `temperature` parameter in the `ChatOpenAI` class to control the randomness of the responses. Lower values make the output more deterministic, while higher values make it more creative.