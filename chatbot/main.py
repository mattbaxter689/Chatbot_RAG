from database.load_docs import LoadDocs
from database.vector_db import VectorDB
from dotenv import load_dotenv
load_dotenv()

#Create the connection to postgres db
vector = VectorDB()

#load documents in specifed directory to the collection
docs = LoadDocs(dir="/docs/")
docs.load_from_dir(vectordb=vector)
