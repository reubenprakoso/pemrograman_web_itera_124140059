"""Pengujian endpoint dengan SQLite sementara dan WebTest."""

import pytest
from pyramid_mahasiswa import main
from pyramid_mahasiswa.models.meta import Base
from webtest import TestApp


@pytest.fixture
def app(tmp_path):
    """Membuat aplikasi tes dan skema SQLite terisolasi untuk setiap tes."""
    database_path = tmp_path / "test.sqlite"
    wsgi_app = main({}, **{"sqlalchemy.url": f"sqlite:///{database_path}"})
    engine = wsgi_app.registry["db_engine"]
    Base.metadata.create_all(engine)
    test_app = TestApp(wsgi_app)
    yield test_app
    engine.dispose()


def test_matakuliah_crud(app):
    """Memverifikasi create, list, detail, update, dan delete matakuliah."""
    payload = {
        "kode_mk": "IF2110",
        "nama_mk": "Pemrograman Web",
        "sks": 3,
        "semester": 3,
    }
    created = app.post_json("/api/matakuliah", payload, status=201).json["matakuliah"]
    item_id = created["id"]
    assert created["kode_mk"] == "IF2110"

    assert app.get("/api/matakuliah").json["matakuliahs"][0]["id"] == item_id
    assert (
        app.get(f"/api/matakuliah/{item_id}").json["matakuliah"]["nama_mk"]
        == "Pemrograman Web"
    )

    updated = app.put_json(f"/api/matakuliah/{item_id}", {"sks": 4}, status=200).json[
        "matakuliah"
    ]
    assert updated["sks"] == 4

    app.delete(f"/api/matakuliah/{item_id}", status=200)
    app.get(f"/api/matakuliah/{item_id}", status=404)


def test_matakuliah_validation(app):
    """Menolak data wajib yang hilang, angka non-positif, dan kode duplikat."""
    app.post_json("/api/matakuliah", {"kode_mk": "IF2110"}, status=400)
    invalid = {"kode_mk": "IF2110", "nama_mk": "Web", "sks": 0, "semester": 3}
    app.post_json("/api/matakuliah", invalid, status=400)

    valid = {"kode_mk": "IF2110", "nama_mk": "Web", "sks": 3, "semester": 3}
    app.post_json("/api/matakuliah", valid, status=201)
    app.post_json("/api/matakuliah", valid, status=400)


def test_mahasiswa_endpoints(app):
    """Memastikan endpoint CRUD mahasiswa tersedia dan tervalidasi."""
    response = app.post_json(
        "/api/mahasiswa",
        {"nim": "124140001", "nama": "Budi", "jurusan": "Informatika"},
        status=201,
    )
    student_id = response.json["mahasiswa"]["id"]
    assert (
        app.get(f"/api/mahasiswa/{student_id}").json["mahasiswa"]["nim"] == "124140001"
    )
    app.put_json(f"/api/mahasiswa/{student_id}", {"nama": "Budi Santoso"}, status=200)
    app.delete(f"/api/mahasiswa/{student_id}", status=200)
