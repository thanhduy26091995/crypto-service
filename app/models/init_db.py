from app.models.database import Base, engine

# Create all tables
Base.metadata.create_all(engine)
