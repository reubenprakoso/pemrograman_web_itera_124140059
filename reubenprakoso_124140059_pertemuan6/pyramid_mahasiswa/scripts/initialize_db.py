"""Inisialisasi dan seeding data contoh ke database."""

import argparse
import logging
import sys
from datetime import date

from pyramid.paster import bootstrap, setup_logging

from ..models import Mahasiswa, Matakuliah

logger = logging.getLogger(__name__)


def setup_models(dbsession) -> None:
    """Tambahkan contoh mahasiswa dan tiga mata kuliah secara idempotent."""
    mahasiswa_seed = (
        {
            "nim": "124140001",
            "nama": "Budi Santoso",
            "jurusan": "Teknik Informatika",
            "tanggal_lahir": "2000-05-15",
            "alamat": "Bandar Lampung",
        },
        {
            "nim": "124140002",
            "nama": "Siti Aminah",
            "jurusan": "Teknik Informatika",
            "tanggal_lahir": "2001-08-22",
            "alamat": "Lampung Selatan",
        },
    )
    matakuliah_seed = (
        {"kode_mk": "IF2110", "nama_mk": "Pemrograman Web", "sks": 3, "semester": 3},
        {"kode_mk": "IF3140", "nama_mk": "Basis Data", "sks": 4, "semester": 5},
        {
            "kode_mk": "IF2210",
            "nama_mk": "Pemrograman Berorientasi Objek",
            "sks": 3,
            "semester": 4,
        },
    )

    for data in mahasiswa_seed:
        if dbsession.query(Mahasiswa).filter_by(nim=data["nim"]).first() is None:
            dbsession.add(
                Mahasiswa(
                    **{
                        **data,
                        "tanggal_lahir": date.fromisoformat(data["tanggal_lahir"]),
                    }
                )
            )

    for data in matakuliah_seed:
        if (
            dbsession.query(Matakuliah).filter_by(kode_mk=data["kode_mk"]).first()
            is None
        ):
            dbsession.add(Matakuliah(**data))


def parse_args(argv: list[str]) -> argparse.Namespace:
    """Membaca lokasi berkas konfigurasi Pyramid dari CLI."""
    parser = argparse.ArgumentParser(description="Seed data contoh aplikasi Pyramid")
    parser.add_argument(
        "config_uri", help="Berkas konfigurasi, misalnya development.ini"
    )
    return parser.parse_args(argv[1:])


def main(argv: list[str] | None = None) -> int:
    """Jalankan seeding melalui transaction manager Pyramid."""
    args = parse_args(argv or sys.argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)
    try:
        with env["request"].tm:
            setup_models(env["request"].dbsession)
        print("Seeding mahasiswa dan minimal 3 matakuliah berhasil.")
        return 0
    except Exception:
        logger.exception("Seeding database gagal.")
        raise
    finally:
        env["closer"]()


if __name__ == "__main__":
    raise SystemExit(main())
