"""Contoh class, instance, atribut class, method, dan dunder methods."""


class Mahasiswa:
    """Merepresentasikan mahasiswa Teknik Informatika ITERA."""

    universitas = "Institut Teknologi Sumatera"
    prodi = "Teknik Informatika"
    total_mahasiswa_terdaftar = 0

    def __init__(self, nama: str, nim: str, ipk: float = 0.0):
        self.nama = nama
        self.nim = nim
        self.ipk = 0.0
        self.daftar_matkul: list[str] = []
        self.update_ipk(ipk)
        Mahasiswa.total_mahasiswa_terdaftar += 1

    def tambah_matkul(self, mata_kuliah: str) -> None:
        """Menambahkan mata kuliah ke daftar milik instance ini."""
        if mata_kuliah.strip():
            self.daftar_matkul.append(mata_kuliah)
            print(f"[{self.nama}] Berhasil mengambil mata kuliah: {mata_kuliah}")

    def update_ipk(self, ipk_baru: float) -> bool:
        """Memperbarui IPK jika berada pada rentang yang valid."""
        if 0.0 <= ipk_baru <= 4.0:
            self.ipk = ipk_baru
            return True
        print(f"Nilai IPK {ipk_baru} tidak valid!")
        return False

    def evaluasi_status(self) -> str:
        """Mengembalikan predikat akademik berdasarkan IPK."""
        if self.ipk >= 3.5:
            return "Cumlaude / Sangat Memuaskan"
        if self.ipk >= 3.0:
            return "Memuaskan"
        if self.ipk >= 2.0:
            return "Cukup"
        return "Perlu Bimbingan Khusus"

    def __str__(self) -> str:
        return f"Mahasiswa: {self.nama} (NIM: {self.nim}) | IPK: {self.ipk:.2f} | Kampus: {self.universitas}"

    def __repr__(self) -> str:
        return f"Mahasiswa(nama={self.nama!r}, nim={self.nim!r}, ipk={self.ipk!r})"


if __name__ == "__main__":
    print("Total mahasiswa awal:", Mahasiswa.total_mahasiswa_terdaftar)
    mhs1 = Mahasiswa("Ahmad Fadhil", "121140001", 3.72)
    mhs2 = Mahasiswa("Nabila Putri", "121140002", 3.40)
    print("Total mahasiswa sekarang:", Mahasiswa.total_mahasiswa_terdaftar)

    mhs1.tambah_matkul("Pemrograman Web")
    mhs1.tambah_matkul("Basis Data")
    mhs2.tambah_matkul("Kecerdasan Buatan")
    print(f"\nMatkul {mhs1.nama}: {mhs1.daftar_matkul}")
    print(f"Matkul {mhs2.nama}: {mhs2.daftar_matkul}")
    print(f"Predikat {mhs1.nama}: {mhs1.evaluasi_status()}")
    print(f"Predikat {mhs2.nama}: {mhs2.evaluasi_status()}")

    print("\nCetak objek mhs1 langsung (memanggil __str__):")
    print(mhs1)
    print("Representasi teknis mhs2 (memanggil __repr__):")
    print(repr(mhs2))

    print("\n--- Modifikasi Atribut Class ---")
    Mahasiswa.universitas = "ITERA Kampus Mandiri"
    print("Kampus mhs1 setelah modifikasi:", mhs1.universitas)
    print("Kampus mhs2 setelah modifikasi:", mhs2.universitas)
