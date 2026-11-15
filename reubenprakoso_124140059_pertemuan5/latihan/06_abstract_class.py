"""Contoh abstract class, abstract property, dan interface database."""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Kontrak abstrak untuk bangun datar."""

    def __init__(self, nama: str):
        self.nama = nama

    @abstractmethod
    def luas(self) -> float:
        """Menghitung luas bangun datar."""
        raise NotImplementedError

    @abstractmethod
    def keliling(self) -> float:
        """Menghitung keliling bangun datar."""
        raise NotImplementedError

    def cetak_laporan(self) -> None:
        """Menampilkan luas dan keliling melalui antarmuka umum."""
        print(
            f"[{self.nama}] Luas: {self.luas():.2f} unit persegi | Keliling: {self.keliling():.2f} unit"
        )


class PersegiPanjang(Shape):
    """Bangun persegi panjang."""

    def __init__(self, panjang: float, lebar: float):
        if panjang <= 0 or lebar <= 0:
            raise ValueError("Panjang dan lebar harus lebih dari 0.")
        super().__init__("Persegi Panjang")
        self.panjang = panjang
        self.lebar = lebar

    def luas(self) -> float:
        return self.panjang * self.lebar

    def keliling(self) -> float:
        return 2 * (self.panjang + self.lebar)


class Lingkaran(Shape):
    """Bangun lingkaran."""

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius harus lebih dari 0.")
        super().__init__("Lingkaran")
        self.radius = radius

    def luas(self) -> float:
        return math.pi * self.radius**2

    def keliling(self) -> float:
        return 2 * math.pi * self.radius


class DatabaseConnector(ABC):
    """Interface yang harus dipenuhi konektor database."""

    @property
    @abstractmethod
    def driver_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def connect(self, host: str, port: int, database: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def execute_query(self, sql: str) -> list:
        raise NotImplementedError

    @abstractmethod
    def disconnect(self) -> None:
        raise NotImplementedError


class PostgreSQLConnector(DatabaseConnector):
    """Simulasi konektor PostgreSQL tanpa membuka koneksi sungguhan."""

    @property
    def driver_name(self) -> str:
        return "PostgreSQL (psycopg2)"

    def connect(self, host: str, port: int, database: str) -> bool:
        print(
            f"[{self.driver_name}] Terhubung ke postgresql://{host}:{port}/{database} [SIMULASI]"
        )
        return True

    def execute_query(self, sql: str) -> list[dict[str, object]]:
        print(f"[{self.driver_name}] Menjalankan SQL: '{sql}' [SIMULASI]")
        return [{"id": 1, "nama": "Ahmad"}, {"id": 2, "nama": "Nabila"}]

    def disconnect(self) -> None:
        print(f"[{self.driver_name}] Koneksi database simulasi ditutup dengan aman.")


if __name__ == "__main__":
    print("--- 1. Uji Coba Kepatuhan Implementasi Shape ---")
    PersegiPanjang(10, 5).cetak_laporan()
    Lingkaran(7).cetak_laporan()

    print("\n--- 2. Pembuktian Enforcement Abstract Class ---")
    try:
        Shape("Bentuk Abstrak")
    except TypeError as err:
        print(f"Penolakan Python Terbukti: {err}")

    class SegitigaCacat(Shape):
        """Subclass demonstrasi yang sengaja belum mengimplementasi keliling."""

        def luas(self) -> float:
            return 0.0

    try:
        SegitigaCacat("Segitiga Cacat")
    except TypeError as err:
        print(f"Penolakan Subclass Cacat: {err}")

    print("\n--- 3. Uji Coba Interface Database Backend ---")
    db = PostgreSQLConnector()
    db.connect("localhost", 5432, "paw_praktikum_db")
    print("Hasil Query Data:", db.execute_query("SELECT id, nama FROM mahasiswa;"))
    db.disconnect()
