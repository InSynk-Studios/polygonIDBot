import os
from embedchain import Pipeline as App
from dotenv import load_dotenv
load_dotenv()

def get_and_init_llm(key):
    os.environ['OPENAI_API_KEY'] = key
    app = App()

    with open('data.txt', 'r') as f:
        text = f.read()

    app.add(text)
    return app

def llm_output(prompt,app):
    return app.query(prompt)

