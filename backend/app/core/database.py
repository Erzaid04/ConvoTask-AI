from collections.abc import Generator

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings


engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def test_connection():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database()")
        )
        database_name = result.scalar()
        print(f"Connected to database: {database_name}")


if __name__ == "__main__":
    test_connection()