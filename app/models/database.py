from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from app.config.settings import settings
from sqlalchemy.orm import sessionmaker

# Database engine
try:
    engine = create_engine(settings.database_url)
    Session = sessionmaker(bind=engine)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Connection successful:", result.fetchone())
except Exception as e:
    print("Connection error: ", e)


# Base class for model
Base = declarative_base()

