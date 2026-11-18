"""Konfigurasi Alembic dengan URL database dari development.ini/env."""

import os
from logging.config import fileConfig

from alembic import context
from pyramid.paster import get_appsettings
from pyramid_mahasiswa.models import Mahasiswa, Matakuliah  # noqa: F401
from pyramid_mahasiswa.models.meta import Base
from sqlalchemy import engine_from_config, pool

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

settings = get_appsettings(config.config_file_name, "main")
database_url = os.environ.get("DATABASE_URL", settings["sqlalchemy.url"])
config.set_main_option("sqlalchemy.url", database_url.replace("%", "%%"))
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Jalankan migrasi tanpa membuat koneksi database langsung."""
    context.configure(
        url=database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Jalankan migrasi memakai koneksi dari SQLAlchemy engine."""
    section = config.get_section(config.config_ini_section) or {}
    section["sqlalchemy.url"] = database_url
    connectable = engine_from_config(
        section,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        future=True,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()
    connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
