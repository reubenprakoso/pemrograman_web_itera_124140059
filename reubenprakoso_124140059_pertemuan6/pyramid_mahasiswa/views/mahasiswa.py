"""REST views CRUD untuk data mahasiswa."""

from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from pyramid.view import view_config

from ..models import Mahasiswa
from .common import json_object, parse_iso_date


def _find_mahasiswa(request, mahasiswa_id: str):
    """Mencari mahasiswa berdasarkan ID numerik dari URL."""
    try:
        parsed_id = int(mahasiswa_id)
    except (TypeError, ValueError):
        return None
    if parsed_id <= 0:
        return None
    return request.dbsession.get(Mahasiswa, parsed_id)


@view_config(route_name="mahasiswa_list", renderer="json")
def mahasiswa_list(request):
    """Mengembalikan semua mahasiswa berdasarkan ID menaik."""
    records = request.dbsession.query(Mahasiswa).order_by(Mahasiswa.id).all()
    return {"mahasiswas": [record.to_dict() for record in records]}


@view_config(route_name="mahasiswa_detail", renderer="json")
def mahasiswa_detail(request):
    """Mengembalikan detail mahasiswa atau HTTP 404."""
    record = _find_mahasiswa(request, request.matchdict["id"])
    if record is None:
        return HTTPNotFound(json_body={"error": "Data mahasiswa tidak ditemukan."})
    return {"mahasiswa": record.to_dict()}


@view_config(route_name="mahasiswa_add", request_method="POST", renderer="json")
def mahasiswa_add(request):
    """Membuat mahasiswa dengan validasi field wajib dan NIM unik."""
    try:
        payload = json_object(request)
        required = ("nim", "nama", "jurusan")
        for field in required:
            if not isinstance(payload.get(field), str) or not payload[field].strip():
                raise ValueError(f"Field {field} wajib diisi dengan teks.")

        nim = payload["nim"].strip()
        if request.dbsession.query(Mahasiswa).filter_by(nim=nim).first():
            raise ValueError("NIM sudah terdaftar.")

        record = Mahasiswa(
            nim=nim,
            nama=payload["nama"].strip(),
            jurusan=payload["jurusan"].strip(),
            tanggal_lahir=parse_iso_date(payload.get("tanggal_lahir")),
            alamat=payload.get("alamat") or None,
        )
        request.dbsession.add(record)
        request.dbsession.flush()
        request.response.status_int = 201
        return {"success": True, "mahasiswa": record.to_dict()}
    except ValueError as error:
        return HTTPBadRequest(json_body={"error": str(error)})


@view_config(route_name="mahasiswa_update", request_method="PUT", renderer="json")
def mahasiswa_update(request):
    """Memperbarui field yang dikirim untuk mahasiswa terpilih."""
    record = _find_mahasiswa(request, request.matchdict["id"])
    if record is None:
        return HTTPNotFound(json_body={"error": "Data mahasiswa tidak ditemukan."})

    try:
        payload = json_object(request)
        for field in ("nim", "nama", "jurusan"):
            if field in payload:
                value = payload[field]
                if not isinstance(value, str) or not value.strip():
                    raise ValueError(f"Field {field} tidak boleh kosong.")
                setattr(record, field, value.strip())

        if "nim" in payload:
            duplicate = (
                request.dbsession.query(Mahasiswa)
                .filter(Mahasiswa.nim == record.nim, Mahasiswa.id != record.id)
                .first()
            )
            if duplicate:
                raise ValueError("NIM sudah digunakan mahasiswa lain.")
        if "tanggal_lahir" in payload:
            record.tanggal_lahir = parse_iso_date(payload["tanggal_lahir"])
        if "alamat" in payload:
            alamat = payload["alamat"]
            if alamat is not None and not isinstance(alamat, str):
                raise ValueError("Field alamat harus berupa teks atau null.")
            record.alamat = alamat or None

        request.dbsession.flush()
        return {"success": True, "mahasiswa": record.to_dict()}
    except ValueError as error:
        return HTTPBadRequest(json_body={"error": str(error)})


@view_config(route_name="mahasiswa_delete", request_method="DELETE", renderer="json")
def mahasiswa_delete(request):
    """Menghapus mahasiswa atau mengembalikan HTTP 404."""
    record = _find_mahasiswa(request, request.matchdict["id"])
    if record is None:
        return HTTPNotFound(json_body={"error": "Data mahasiswa tidak ditemukan."})
    request.dbsession.delete(record)
    return {"success": True, "message": "Data mahasiswa berhasil dihapus."}
