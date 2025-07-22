from langchain.chat_models import init_chat_model
from models.abstract_model import AbstractModel
from dotenv import load_dotenv
from tools.tools import tools_list

class OpenAIModel(AbstractModel):    
    def __init__(self):
        load_dotenv()
        self.llm = init_chat_model("openai:gpt-4.1")
        self.llm_with_tools = self.llm.bind_tools(tools_list)
        
    def invoke(self, messages: list):
        return self.llm.invoke(messages)
    
    def invoke_with_tools(self, messages: list):
        return self.llm_with_tools.invoke(messages)