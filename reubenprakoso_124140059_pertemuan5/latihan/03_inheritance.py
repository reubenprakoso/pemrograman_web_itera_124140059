"""Contoh inheritance, overriding, super(), dan multiple inheritance."""


class Kendaraan:
    """Superclass yang menyimpan karakteristik umum kendaraan."""

    def __init__(self, merek: str, model: str, tahun: int):
        self.merek = merek
        self.model = model
        self.tahun = tahun
        self.odometer = 0.0

    def deskripsi(self) -> str:
        return f"{self.merek} {self.model} ({self.tahun})"

    def tambah_jarak(self, km: float) -> None:
        if km > 0:
            self.odometer += km
            print(f"[{self.merek}] Menempuh perjalanan +{km} km. Total Odo: {self.odometer} km")
        else:
            print("Nilai kilometer tambahan tidak valid!")

    def klakson(self) -> str:
        return "Tin tin!"


class Mobil(Kendaraan):
    """Kendaraan roda empat dengan jumlah pintu dan tangki bahan bakar."""

    def __init__(self, merek: str, model: str, tahun: int, jumlah_pintu: int, kapasitas_tangki: float):
        super().__init__(merek, model, tahun)
        if jumlah_pintu <= 0 or kapasitas_tangki < 0:
            raise ValueError("Jumlah pintu harus positif dan kapasitas tangki tidak boleh negatif.")
        self.jumlah_pintu = jumlah_pintu
        self.kapasitas_tangki = kapasitas_tangki
        self.sisa_bensin = 0.0

    def deskripsi(self) -> str:
        return f"{super().deskripsi()} [Mobil {self.jumlah_pintu} Pintu, Tangki: {self.kapasitas_tangki}L]"

    def klakson(self) -> str:
        return "Telolet! Telolet! (Klakson Mobil)"

    def isi_bensin(self, liter: float) -> bool:
        if liter <= 0:
            print("Jumlah bensin harus lebih dari 0L.")
            return False
        if self.sisa_bensin + liter > self.kapasitas_tangki:
            print("Kapasitas tangki bensin akan meluap!")
            return False
        self.sisa_bensin += liter
        print(f"[{self.merek} {self.model}] Diisi bensin {liter}L. Sisa bahan bakar: {self.sisa_bensin}L")
        return True


class Motor(Kendaraan):
    """Kendaraan roda dua dengan kapasitas mesin tertentu."""

    def __init__(self, merek: str, model: str, tahun: int, kapasitas_cc: int):
        super().__init__(merek, model, tahun)
        self.kapasitas_cc = kapasitas_cc

    def deskripsi(self) -> str:
        return f"{super().deskripsi()} [Motor Sport {self.kapasitas_cc}cc]"

    def klakson(self) -> str:
        return "Bip bip! (Klakson Motor)"

    def wheelie(self) -> None:
        print(f"[{self.merek} {self.model}] Melakukan atraksi wheelie satu roda!")


class KomponenBaterai:
    """Mixin untuk menyimpan dan mengisi daya baterai kendaraan listrik."""

    def __init__(self, kapasitas_kwh: float):
        if kapasitas_kwh <= 0:
            raise ValueError("Kapasitas baterai harus lebih dari 0 kWh.")
        self.kapasitas_kwh = kapasitas_kwh
        self.daya_tersisa = 100.0

    def isi_daya(self, persen: float) -> None:
        if persen <= 0:
            print("Persentase pengisian harus lebih dari 0.")
            return
        self.daya_tersisa = min(100.0, self.daya_tersisa + persen)
        print(f"Baterai diisi ulang. Kapasitas daya: {self.daya_tersisa}%")


class MobilListrik(Mobil, KomponenBaterai):
    """Mobil yang juga memiliki kemampuan komponen baterai."""

    def __init__(self, merek: str, model: str, tahun: int, kapasitas_kwh: float):
        Mobil.__init__(self, merek, model, tahun, jumlah_pintu=4, kapasitas_tangki=0.0)
        KomponenBaterai.__init__(self, kapasitas_kwh)

    def deskripsi(self) -> str:
        return (
            f"{self.merek} {self.model} ({self.tahun}) "
            f"[EV Baterai {self.kapasitas_kwh} kWh, Daya: {self.daya_tersisa}%]"
        )


if __name__ == "__main__":
    avanza = Mobil("Toyota", "Avanza Veloz", 2023, jumlah_pintu=5, kapasitas_tangki=45.0)
    cbr = Motor("Honda", "CBR250RR", 2022, kapasitas_cc=250)
    ioniq = MobilListrik("Hyundai", "Ioniq 5", 2024, kapasitas_kwh=72.6)

    print("--- Deskripsi Kendaraan ---")
    print(avanza.deskripsi())
    print(cbr.deskripsi())
    print(ioniq.deskripsi())
    print("\n--- Uji Coba Suara Klakson ---")
    print(f"{avanza.model} : {avanza.klakson()}")
    print(f"{cbr.model}    : {cbr.klakson()}")
    print("\n--- Perjalanan & Konsumsi Energi ---")
    avanza.tambah_jarak(120.5)
    avanza.isi_bensin(15)
    cbr.wheelie()
    ioniq.isi_daya(30)
    print("\n--- Pemeriksaan Relasi Pewarisan ---")
    print("Apakah avanza adalah instance dari Mobil?    :", isinstance(avanza, Mobil))
    print("Apakah avanza adalah instance dari Kendaraan?:", isinstance(avanza, Kendaraan))
    print("Apakah cbr adalah instance dari Mobil?       :", isinstance(cbr, Mobil))
    print("Apakah Mobil subclass dari Kendaraan?        :", issubclass(Mobil, Kendaraan))
    print("MRO MobilListrik:", [cls.__name__ for cls in MobilListrik.__mro__])
