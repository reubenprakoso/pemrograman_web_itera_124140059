"""REST views CRUD untuk data matakuliah."""

from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from pyramid.view import view_config

from ..models import Matakuliah
from .common import json_object, positive_integer

_REQUIRED_FIELDS = ("kode_mk", "nama_mk", "sks", "semester")


def _find_matakuliah(request, matakuliah_id: str):
    """Mencari mata kuliah berdasarkan ID numerik dari URL."""
    try:
        parsed_id = int(matakuliah_id)
    except (TypeError, ValueError):
        return None
    if parsed_id <= 0:
        return None
    return request.dbsession.get(Matakuliah, parsed_id)


def _validate_text(payload: dict, field: str, required: bool = False):
    """Memvalidasi nilai kode atau nama mata kuliah."""
    value = payload.get(field)
    if value is None and not required:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Field {field} wajib diisi dengan teks.")
    return value.strip()


def _validate_unique_code(request, code: str, exclude_id: int | None = None) -> None:
    """Menolak kode matakuliah yang sudah dipakai record lain."""
    query = request.dbsession.query(Matakuliah).filter_by(kode_mk=code)
    if exclude_id is not None:
        query = query.filter(Matakuliah.id != exclude_id)
    if query.first():
        raise ValueError("kode_mk sudah terdaftar.")


@view_config(route_name="matakuliah_list", renderer="json")
def matakuliah_list(request):
    """Mengembalikan semua mata kuliah berdasarkan ID menaik."""
    records = request.dbsession.query(Matakuliah).order_by(Matakuliah.id).all()
    return {"matakuliahs": [record.to_dict() for record in records]}


@view_config(route_name="matakuliah_detail", renderer="json")
def matakuliah_detail(request):
    """Mengembalikan detail matakuliah atau HTTP 404."""
    record = _find_matakuliah(request, request.matchdict["id"])
    if record is None:
        return HTTPNotFound(json_body={"error": "Data matakuliah tidak ditemukan."})
    return {"matakuliah": record.to_dict()}


@view_config(route_name="matakuliah_add", request_method="POST", renderer="json")
def matakuliah_add(request):
    """Menambahkan mata kuliah dan memastikan SKS/semester positif."""
    try:
        payload = json_object(request)
        for field in _REQUIRED_FIELDS:
            if field not in payload:
                raise ValueError(f"Field {field} wajib diisi.")

        kode_mk = _validate_text(payload, "kode_mk", required=True)
        nama_mk = _validate_text(payload, "nama_mk", required=True)
        sks = positive_integer(payload["sks"], "sks")
        semester = positive_integer(payload["semester"], "semester")
        _validate_unique_code(request, kode_mk)

        record = Matakuliah(
            kode_mk=kode_mk.upper(),
            nama_mk=nama_mk,
            sks=sks,
            semester=semester,
        )
        request.dbsession.add(record)
        request.dbsession.flush()
        request.response.status_int = 201
        return {"success": True, "matakuliah": record.to_dict()}
    except ValueError as error:
        return HTTPBadRequest(json_body={"error": str(error)})


@view_config(route_name="matakuliah_update", request_method="PUT", renderer="json")
def matakuliah_update(request):
    """Memperbarui sebagian atau seluruh field mata kuliah."""
    record = _find_matakuliah(request, request.matchdict["id"])
    if record is None:
        return HTTPNotFound(json_body={"error": "Data matakuliah tidak ditemukan."})

    try:
        payload = json_object(request)
        if "kode_mk" in payload:
            kode_mk = _validate_text(payload, "kode_mk", required=True).upper()
            _validate_unique_code(request, kode_mk, exclude_id=record.id)
            record.kode_mk = kode_mk
        if "nama_mk" in payload:
            record.nama_mk = _validate_text(payload, "nama_mk", required=True)
        if "sks" in payload:
            record.sks = positive_integer(payload["sks"], "sks")
        if "semester" in payload:
            record.semester = positive_integer(payload["semester"], "semester")

        request.dbsession.flush()
        return {"success": True, "matakuliah": record.to_dict()}
    except ValueError as error:
        return HTTPBadRequest(json_body={"error": str(error)})


@view_config(route_name="matakuliah_delete", request_method="DELETE", renderer="json")
def matakuliah_delete(request):
    """Menghapus mata kuliah atau mengembalikan HTTP 404."""
    record = _find_matakuliah(request, request.matchdict["id"])
    if record is None:
        return HTTPNotFound(json_body={"error": "Data matakuliah tidak ditemukan."})
    request.dbsession.delete(record)
    return {"success": True, "message": "Data matakuliah berhasil dihapus."}
