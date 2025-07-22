from models.openai_model import OpenAIModel

def test_openai_model_creation():
    first_model = OpenAIModel()
    second_model = OpenAIModel()
    print(first_model == second_model)
    
test_openai_model_creation()