"""Base declarative SQLAlchemy untuk seluruh model aplikasi."""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base metadata ORM yang dipakai oleh Alembic dan model."""
