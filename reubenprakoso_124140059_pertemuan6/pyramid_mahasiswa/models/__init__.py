"""Konfigurasi SQLAlchemy dan request-scoped session Pyramid."""

import zope.sqlalchemy
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

from .mahasiswa import Mahasiswa
from .matakuliah import Matakuliah
from .meta import Base


def includeme(config):
    """Buat engine dan sediakan session yang mengikuti transaksi request."""
    settings = config.get_settings()
    engine = engine_from_config(settings, prefix="sqlalchemy.", future=True)
    session_factory = sessionmaker(bind=engine, expire_on_commit=False)
    config.registry["dbsession_factory"] = session_factory
    config.registry["db_engine"] = engine

    def get_dbsession(request):
        session = session_factory()
        zope.sqlalchemy.register(session, transaction_manager=request.tm)
        return session

    config.add_request_method(get_dbsession, "dbsession", reify=True)
