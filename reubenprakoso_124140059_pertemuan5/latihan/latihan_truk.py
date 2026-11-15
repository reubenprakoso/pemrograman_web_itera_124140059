"""Latihan mandiri inheritance untuk truk ekspedisi."""

from __future__ import annotations


class Kendaraan:
    """Kendaraan umum sebagai superclass."""

    def __init__(self, merek: str, model: str, tahun: int):
        self.merek = merek
        self.model = model
        self.tahun = tahun

    def deskripsi(self) -> str:
        """Menghasilkan deskripsi standar kendaraan."""
        return f"{self.merek} {self.model} ({self.tahun})"


class Truk(Kendaraan):
    """Kendaraan angkut dengan batas muatan dalam ton."""

    def __init__(
        self, merek: str, model: str, tahun: int, kapasitas_maksimal_ton: float
    ):
        super().__init__(merek, model, tahun)
        if kapasitas_maksimal_ton <= 0:
            raise ValueError("Kapasitas maksimal harus lebih dari 0 ton.")
        self.kapasitas_maksimal_ton = kapasitas_maksimal_ton
        self.muatan_saat_ini = 0.0

    def muat_barang(self, berat_ton: float) -> bool:
        """Menambahkan muatan jika jumlahnya tidak melewati kapasitas truk."""
        if berat_ton <= 0:
            print("Berat muatan harus lebih dari 0 ton.")
            return False
        if self.muatan_saat_ini + berat_ton > self.kapasitas_maksimal_ton:
            print("Gagal memuat: kapasitas maksimal truk akan terlampaui.")
            return False
        self.muatan_saat_ini += berat_ton
        print(f"Muatan bertambah {berat_ton} ton. Total: {self.muatan_saat_ini} ton.")
        return True

    def deskripsi(self) -> str:
        """Override deskripsi kendaraan dengan informasi muatan."""
        return (
            f"{super().deskripsi()} | Muatan: {self.muatan_saat_ini}/"
            f"{self.kapasitas_maksimal_ton} ton"
        )


if __name__ == "__main__":
    truk = Truk("Mitsubishi", "Fuso", 2024, 8)
    truk.muat_barang(3.5)
    truk.muat_barang(5)
    print(truk.deskripsi())
