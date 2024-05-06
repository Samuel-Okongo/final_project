import click
from app.models import get_db_session  # Adjust based on your actual import paths
from sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Adjust the database URL as per your configuration
engine = create_engine('postgresql://user:password@localhost:5432/mydatabase', echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# db_session should not be a single instance but generated per request/session in use
def get_db_session():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

@click.group(name='db')
def database_cli():
    """Commands related to database management."""
    pass

@database_cli.command(name='drop')
def drop_tables():
    """Drop all database tables including Alembic ones for a reset."""
    with get_db_session() as db_session:
        db_session.drop_all()
        db_session.commit()  # Always commit changes
    click.echo("All tables dropped successfully.")

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
# Add more database-related commands here
