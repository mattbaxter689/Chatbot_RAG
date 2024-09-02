from dotenv import load_dotenv
from pydantic import BaseModel
import os


class DBParameters(BaseModel):
    pg_user: str
    pg_pass: str
    pg_port: str
    pg_db: str
    pg_host: str


class DBConn:
    def __init__(self) -> None:
        load_dotenv()
        self.dbparams = DBParameters(
            pg_user=os.environ["POSTGRES_USER"],
            pg_pass=os.environ["POSTGRES_PASSWORD"],
            pg_db=os.environ["POSTGRES_DB"],
            pg_port=os.environ["POSTGRES_PORT"],
            pg_host=os.environ["POSTGRES_HOST"],
        )

    def __call__(self) -> str:
        return f"postgresql+psycopg://{self.dbparams.pg_user}:{self.dbparams.pg_pass}@{self.dbparams.pg_host}:{self.dbparams.pg_port}/{self.dbparams.pg_db}"
