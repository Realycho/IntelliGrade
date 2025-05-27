from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings # Assuming settings will have DATABASE_URL

# For PostgreSQL, the DATABASE_URL would be like:
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@host:port/database"

# We will use the DATABASE_URL from settings.
# Ensure that settings.DATABASE_URL is configured appropriately later.
# If DATABASE_URL is not yet in settings, this might raise an AttributeError
# For now, we'll assume it will be added.
SQLALCHEMY_DATABASE_URL = getattr(settings, "DATABASE_URL", "postgresql://user:password@host:port/database_placeholder")


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # For PostgreSQL, connect_args are typically not needed for basic setup.
    # If specific driver options or pool settings are required, they can be added here
    # or directly in create_engine parameters like pool_size.
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
