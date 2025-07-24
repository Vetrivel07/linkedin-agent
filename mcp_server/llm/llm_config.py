from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model_name="gpt-4o",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)
def get_llm():
    return ChatOpenAI(
        model="gpt-4o",
        temperature=0.7,
        max_tokens=300
    )