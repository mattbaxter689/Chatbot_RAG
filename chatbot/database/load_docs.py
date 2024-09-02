from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from database.vector_db import VectorDB
import os
import uuid
from dotenv import load_dotenv
load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.environ["HUGGINGFACE_ACCESS"]


class LoadDocs:
    def __init__(self, dir: str) -> None:
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=20,
            length_function=len,
            is_separator_regex=False,
        )
        self.dir = dir

    def load_from_dir(self, vectordb: VectorDB):
        full_path = os.getcwd() + self.dir
        for file in os.listdir(full_path):
            if file.endswith(".pdf"):
                loader = PyPDFLoader(full_path+file)
                docs = loader.load()
                splits = self.text_splitter.split_documents(docs)
                print(splits)
                uuids = [str(uuid.uuid4()) for _ in range(len(splits))]
                vectordb().add_documents(documents=splits, ids=uuids)
