"""Model ORM Matakuliah dengan validasi constraint database."""

from sqlalchemy import CheckConstraint, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .meta import Base


class Matakuliah(Base):
    """Mewakili mata kuliah dengan kode unik dan beban akademik positif."""

    __tablename__ = "matakuliah"
    __table_args__ = (
        CheckConstraint("sks > 0", name="ck_matakuliah_sks_positive"),
        CheckConstraint("semester > 0", name="ck_matakuliah_semester_positive"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    kode_mk: Mapped[str] = mapped_column(String(20), unique=True, nullable=False, index=True)
    nama_mk: Mapped[str] = mapped_column(String(150), nullable=False)
    sks: Mapped[int] = mapped_column(Integer, nullable=False)
    semester: Mapped[int] = mapped_column(Integer, nullable=False)

    def to_dict(self) -> dict[str, int | str]:
        """Mengubah data mata kuliah menjadi dictionary untuk respons JSON."""
        return {
            "id": self.id,
            "kode_mk": self.kode_mk,
            "nama_mk": self.nama_mk,
            "sks": self.sks,
            "semester": self.semester,
        }
