from langchain_chroma import Chroma

from src.components.embeddings import embeddings
from src.settings import settings

vectorstore = Chroma(
    collection_name=settings.COLLECTION_NAME,
    persist_directory=settings.PERSIST_DIRECTORY,
    embedding_function=embeddings
)