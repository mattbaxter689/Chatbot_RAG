from langchain_postgres.vectorstores import PGVector
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from database.db_conn import DBConn


class VectorDB:
    def __init__(self, collection_name: str = "chatbotv1") -> None:
        self.dbconn = DBConn()
        self.collection_name = collection_name
        self.vectordb = PGVector(
            collection_name=self.collection_name,
            connection=self.dbconn(),
            embeddings=HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-miniLM-L6-v2"
            ),
        )

    def __call__(
        self,
    ) -> PGVector:
        return self.vectordb
