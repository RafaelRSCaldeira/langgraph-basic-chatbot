from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

class OpenAIModel():
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        load_dotenv()
        self.model = init_chat_model("openai:gpt-4.1")
        
    def generate_answer():
        return "Operação realizada por: ", OpenAIModel._instance.model