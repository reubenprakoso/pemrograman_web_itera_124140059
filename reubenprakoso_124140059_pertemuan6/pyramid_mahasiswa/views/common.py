"""Utilitas validasi input bersama untuk endpoint REST."""

from datetime import date


def json_object(request) -> dict:
    """Membaca body JSON dan menolak payload non-object atau JSON invalid."""
    try:
        payload = request.json_body
    except (ValueError, TypeError) as error:
        raise ValueError("Body request harus berupa JSON yang valid.") from error
    if not isinstance(payload, dict):
        raise ValueError("Body JSON harus berupa object.")
    return payload


def positive_integer(value, field_name: str) -> int:
    """Memastikan nilai integer positif dan bukan boolean."""
    if isinstance(value, bool):
        raise ValueError(f"Field {field_name} harus berupa bilangan bulat positif.")
    try:
        parsed = int(value)
    except (TypeError, ValueError) as error:
        raise ValueError(
            f"Field {field_name} harus berupa bilangan bulat positif."
        ) from error
    if str(value).strip() != str(parsed) or parsed <= 0:
        raise ValueError(f"Field {field_name} harus berupa bilangan bulat positif.")
    return parsed


def parse_iso_date(value, field_name: str = "tanggal_lahir") -> date | None:
    """Mengubah tanggal ISO YYYY-MM-DD menjadi date atau None."""
    if value in (None, ""):
        return None
    if not isinstance(value, str):
        raise ValueError(f"Field {field_name} harus memakai format YYYY-MM-DD.")
    try:
        return date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(
            f"Format {field_name} tidak valid. Gunakan YYYY-MM-DD."
        ) from error
