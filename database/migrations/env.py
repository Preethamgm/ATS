from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import the database and models
from app.database import Base
from app.models import Job, Applicant, Application  # Import all models

# Get Alembic Config object, which provides access to `alembic.ini`
config = context.config

# Set database URL from .env instead of hardcoding it in alembic.ini
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/ats_db")
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Configure logging using `alembic.ini`
if config.config_file_name:
    fileConfig(config.config_file_name)

# Set metadata for autogenerate
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode (without a DB connection)."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode (with a DB connection)."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

# Decide whether to run online or offline migrations
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
