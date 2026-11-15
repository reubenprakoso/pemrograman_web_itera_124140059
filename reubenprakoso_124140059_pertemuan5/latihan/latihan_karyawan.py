"""Latihan mandiri encapsulation gaji karyawan dengan property."""


class Karyawan:
    """Menyimpan data karyawan dan menjaga batas minimum gaji pokok."""

    UMR_MINIMUM = 3_200_000

    def __init__(self, nama: str, jabatan: str, gaji_pokok: float):
        self.nama = nama
        self.jabatan = jabatan
        self.__gaji_pokok = self.UMR_MINIMUM
        self.gaji_pokok = gaji_pokok

    @property
    def gaji_pokok(self) -> float:
        """Mengambil gaji pokok melalui property read-only terkendali."""
        return self.__gaji_pokok

    @gaji_pokok.setter
    def gaji_pokok(self, nilai: float) -> None:
        if isinstance(nilai, bool) or not isinstance(nilai, (int, float)):
            raise TypeError("Gaji pokok harus berupa angka.")
        if nilai < self.UMR_MINIMUM:
            raise ValueError(f"Gaji pokok minimal Rp {self.UMR_MINIMUM:,.0f}.")
        self.__gaji_pokok = float(nilai)

    def hitung_gaji_bersih(self, pajak_persen: float) -> float:
        """Menghitung gaji setelah potongan pajak persentase."""
        if not 0 <= pajak_persen <= 100:
            raise ValueError("Pajak harus berada pada rentang 0 hingga 100 persen.")
        return self.gaji_pokok * (1 - pajak_persen / 100)


if __name__ == "__main__":
    karyawan = Karyawan("Siti Rahma", "Programmer", 5_000_000)
    print(f"{karyawan.nama} - {karyawan.jabatan}")
    print(f"Gaji bersih setelah pajak 5%: Rp {karyawan.hitung_gaji_bersih(5):,.0f}")
    try:
        karyawan.gaji_pokok = 3_000_000
    except ValueError as err:
        print("Validasi gaji:", err)
