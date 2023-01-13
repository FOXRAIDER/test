from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

SQLALCHEMY_DATABASE_URL = URL.create(
        "postgresql+psycopg2",
        username="PGUSER",
        # password="postgrespw",
        password="PGPASSWORD",
        # host="db",
        host="localhost",
        port=5432,
        # database="tg_bot"
        database="PGDB"
    )
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()