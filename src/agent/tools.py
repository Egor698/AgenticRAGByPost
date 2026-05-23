from langchain.tools import tool

from src.components.vector_store import vectorstore

@tool(description='Поиск релевантной информации соответствующей запросу')
def retrieve(query: str) -> str:
    retrieved_docs = vectorstore.similarity_search(query, k=4)
    
    serialized = "\n\n".join(f"Source: {doc.metadata}\nContent:{doc.page_content}"
                             for doc in retrieved_docs)
    
    return serialized