"""Endpoint sederhana untuk memeriksa status layanan."""

from pyramid.view import view_config


@view_config(route_name="home", renderer="json")
def home(request):
    """Mengembalikan nama layanan dan resource API yang tersedia."""
    return {
        "application": "Pyramid Mahasiswa API",
        "status": "ok",
        "endpoints": ["/api/mahasiswa", "/api/matakuliah"],
    }
