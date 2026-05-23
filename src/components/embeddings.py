from langchain_openai import OpenAIEmbeddings

from src.settings import settings 

embeddings = OpenAIEmbeddings(
    api_key=settings.OPENAI_API_KEY,
    base_url=settings.BASE_URL,
    model="openai/text-embedding-3-small"
)