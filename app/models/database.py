from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app.config.settings import settings
from sqlalchemy.orm import sessionmaker

# Database engine
engine = create_engine(settings.database_url)
Session = sessionmaker(bind=engine)

# Base class for model
Base = declarative_base()

