from sqlalchemy import create_engine, text

from app.core.config import settings


engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)


def test_connection():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database()")
        )

        database_name = result.scalar()

        print(f"Connected to database: {database_name}")


if __name__ == "__main__":
    test_connection()