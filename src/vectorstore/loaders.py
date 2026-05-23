import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import CharacterTextSplitter

from src.components.vector_store import vectorstore

loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    )
)

docs = loader.load()


text_splitter = CharacterTextSplitter(separator='', chunk_size=1100, chunk_overlap=300)
all_splits = text_splitter.split_documents(docs)

vectorstore.add_documents(all_splits)



