from abc import ABC, abstractmethod

class AbstractModel(ABC):
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @abstractmethod
    def invoke(self, messages: list):
        pass
    
    @abstractmethod
    def invoke_with_tools(self, messages: list):
        pass