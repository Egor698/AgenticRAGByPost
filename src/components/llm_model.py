from langchain_openai import ChatOpenAI

from src.settings import settings 

llm = ChatOpenAI(
    api_key=settings.OPENAI_API_KEY,
    base_url=settings.BASE_URL,
    model="openai/gpt-4o-mini",
)