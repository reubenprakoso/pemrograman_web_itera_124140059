"""Membandingkan pengelolaan data mahasiswa secara prosedural dan OOP."""

mahasiswa_proc = {
    "nama": "Budi Santoso",
    "nim": "121140001",
    "jurusan": "Teknik Informatika",
    "ipk": 3.45,
}


def cetak_profil_prosedural(mhs: dict) -> None:
    """Menampilkan profil dari dictionary mahasiswa."""
    print(f"[Prosedural] {mhs['nama']} ({mhs['nim']}) - {mhs['jurusan']} | IPK: {mhs['ipk']}")


def perbarui_ipk_prosedural(mhs: dict, ipk_baru: float) -> bool:
    """Memperbarui IPK jika nilainya berada pada rentang 0 sampai 4."""
    if 0.0 <= ipk_baru <= 4.0:
        mhs["ipk"] = ipk_baru
        return True
    print("Nilai IPK tidak valid!")
    return False


class Mahasiswa:
    """Menyimpan data dan perilaku dasar seorang mahasiswa."""

    def __init__(self, nama: str, nim: str, jurusan: str, ipk: float):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = 0.0
        self.update_ipk(ipk)

    def cetak_profil(self) -> None:
        """Menampilkan profil mahasiswa ini."""
        print(f"[OOP] {self.nama} ({self.nim}) - {self.jurusan} | IPK: {self.ipk}")

    def update_ipk(self, ipk_baru: float) -> bool:
        """Menerapkan perubahan IPK dengan validasi rentang."""
        if 0.0 <= ipk_baru <= 4.0:
            self.ipk = ipk_baru
            print(f"IPK {self.nama} berhasil diperbarui menjadi {self.ipk}")
            return True
        print("Peringatan: Nilai IPK harus berada pada rentang 0.0 s.d 4.0!")
        return False


if __name__ == "__main__":
    cetak_profil_prosedural(mahasiswa_proc)
    perbarui_ipk_prosedural(mahasiswa_proc, 3.75)
    cetak_profil_prosedural(mahasiswa_proc)

    print("\n--- Eksekusi Paradigma OOP ---")
    mhs_oop = Mahasiswa("Siti Rahma", "121140002", "Teknik Informatika", 3.80)
    mhs_oop.cetak_profil()
    mhs_oop.update_ipk(3.92)
    mhs_oop.cetak_profil()
