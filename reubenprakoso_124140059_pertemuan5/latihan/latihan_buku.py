"""Latihan mandiri class Buku, diskon, dan dunder method __len__."""


class Buku:
    """Menyimpan informasi buku dan menyediakan perhitungan harga diskon."""

    def __init__(
        self, judul: str, penulis: str, harga_asli: float, jumlah_halaman: int
    ):
        if harga_asli < 0 or jumlah_halaman < 0:
            raise ValueError("Harga dan jumlah halaman tidak boleh negatif.")
        self.judul = judul
        self.penulis = penulis
        self.harga_asli = harga_asli
        self.jumlah_halaman = jumlah_halaman

    def hitung_harga_diskon(self, persen: float) -> float:
        """Mengembalikan harga setelah diskon 0 hingga 100 persen."""
        if not 0 <= persen <= 100:
            raise ValueError(
                "Persentase diskon harus berada pada rentang 0 hingga 100."
            )
        return self.harga_asli * (1 - persen / 100)

    def __len__(self) -> int:
        return self.jumlah_halaman

    def __str__(self) -> str:
        return (
            f"{self.judul} karya {self.penulis} | "
            f"Harga: Rp {self.harga_asli:,.0f} | {self.jumlah_halaman} halaman"
        )


if __name__ == "__main__":
    buku = Buku("Belajar Python", "Tim Praktikum", 120000, 240)
    print(buku)
    print(f"Harga setelah diskon 15%: Rp {buku.hitung_harga_diskon(15):,.0f}")
    print("Jumlah halaman via len(buku):", len(buku))
