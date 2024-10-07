# app.py
import logging
from models import Base
from db_config import engine, Session
import seed

# Configure logging to display SQL statements
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)  # Set to DEBUG for more details


def create_tables():
    Base.metadata.create_all(engine)
    print("Database tables created.")

def main():
    """
    Main function to execute the seed data.
    """
    # Створити таблиці
    create_tables()

    # Заповнити базу даних
    with Session() as session:
        seed.seed_data(session)


if __name__ == "__main__":
    main()
