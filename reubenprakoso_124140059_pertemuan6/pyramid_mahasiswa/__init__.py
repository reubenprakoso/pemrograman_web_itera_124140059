"""Factory aplikasi Pyramid untuk REST API praktikum."""

import os

from pyramid.config import Configurator


def main(global_config, **settings):
    """Membuat aplikasi WSGI dan mengatur routes, database, serta views."""
    settings["sqlalchemy.url"] = os.environ.get(
        "DATABASE_URL", settings.get("sqlalchemy.url", "")
    )
    with Configurator(settings=settings) as config:
        config.include("pyramid_tm")
        config.include(".models")
        config.include(".routes")
        config.scan("pyramid_mahasiswa.views")
        return config.make_wsgi_app()
