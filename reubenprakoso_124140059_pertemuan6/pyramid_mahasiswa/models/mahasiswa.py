"""Model ORM Mahasiswa."""

from datetime import date

from sqlalchemy import Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .meta import Base


class Mahasiswa(Base):
    """Mewakili mahasiswa dan kolom tabel mahasiswa."""

    __tablename__ = "mahasiswa"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nim: Mapped[str] = mapped_column(String(32), unique=True, nullable=False, index=True)
    nama: Mapped[str] = mapped_column(String(120), nullable=False)
    jurusan: Mapped[str] = mapped_column(String(120), nullable=False)
    tanggal_lahir: Mapped[date | None] = mapped_column(Date, nullable=True)
    alamat: Mapped[str | None] = mapped_column(String(255), nullable=True)

    def to_dict(self) -> dict[str, object]:
        """Mengubah data mahasiswa menjadi dictionary yang dapat dijadikan JSON."""
        return {
            "id": self.id,
            "nim": self.nim,
            "nama": self.nama,
            "jurusan": self.jurusan,
            "tanggal_lahir": self.tanggal_lahir.isoformat() if self.tanggal_lahir else None,
            "alamat": self.alamat,
        }
