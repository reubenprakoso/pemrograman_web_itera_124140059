"""Contoh encapsulation, name mangling, dan validasi dengan property."""


class RekeningBank:
    """Rekening sederhana dengan saldo dan PIN yang dilindungi."""

    def __init__(self, nomor_rekening: str, nama_pemilik: str, saldo_awal: float, pin: str):
        if saldo_awal < 0:
            raise ValueError("Saldo awal tidak boleh negatif.")
        self.nomor_rekening = nomor_rekening
        self._pemilik = nama_pemilik
        self.__saldo = float(saldo_awal)
        self.__pin = str(pin)
        self._riwayat_transaksi: list[str] = []

    @property
    def saldo(self) -> float:
        """Mengembalikan saldo untuk dibaca tanpa membuka atribut internal."""
        return self.__saldo

    @saldo.setter
    def saldo(self, jumlah_baru: float) -> None:
        if isinstance(jumlah_baru, bool) or not isinstance(jumlah_baru, (int, float)):
            raise TypeError("Nilai saldo harus berupa angka numerik!")
        if jumlah_baru < 0:
            raise ValueError("Saldo rekening tidak boleh bernilai negatif!")
        self.__saldo = float(jumlah_baru)
        print(f"[AUDIT] Saldo {self.nomor_rekening} disesuaikan menjadi: Rp {self.__saldo:,.2f}")

    def setor(self, nominal: float) -> bool:
        """Menambah saldo dan mencatat transaksi setoran yang valid."""
        if nominal <= 0:
            print("Gagal: Nominal setor harus lebih besar dari Rp 0!")
            return False
        self.__saldo += nominal
        self._riwayat_transaksi.append(f"Setor Tunai: +Rp {nominal:,.2f}")
        print(f"Setor tunai Rp {nominal:,.2f} sukses. Saldo saat ini: Rp {self.__saldo:,.2f}")
        return True

    def tarik(self, nominal: float, pin_input: str) -> bool:
        """Menarik uang hanya jika PIN, nominal, dan saldo memenuhi syarat."""
        if pin_input != self.__pin:
            print("Gagal: PIN Transaksi yang Anda masukkan salah!")
            return False
        if nominal <= 0:
            print("Gagal: Nominal penarikan harus lebih dari Rp 0!")
            return False
        if nominal > self.__saldo:
            print(f"Gagal: Saldo tidak mencukupi! (Saldo: Rp {self.__saldo:,.2f}, Tarik: Rp {nominal:,.2f})")
            return False
        self.__saldo -= nominal
        self._riwayat_transaksi.append(f"Tarik Tunai: -Rp {nominal:,.2f}")
        print(f"Tarik tunai Rp {nominal:,.2f} berhasil. Sisa saldo: Rp {self.__saldo:,.2f}")
        return True

    def cetak_mutasi(self) -> None:
        """Menampilkan transaksi dan saldo akhir rekening."""
        print(f"\n=== MUTASI REKENING {self.nomor_rekening} ({self._pemilik}) ===")
        for log in self._riwayat_transaksi:
            print(f" - {log}")
        print(f"Saldo Akhir Terverifikasi: Rp {self.__saldo:,.2f}\n")


if __name__ == "__main__":
    rek = RekeningBank("121-009-8871", "Ahmad Fadhilah", 500000, "123456")
    print("Nomor Rekening (Public) :", rek.nomor_rekening)
    print("Pemilik Rekening (Prot) :", rek._pemilik)
    print("Saldo Rekening (@prop)  : Rp", rek.saldo)

    rek.setor(250000)
    rek.tarik(100000, "999999")
    rek.tarik(100000, "123456")
    rek.tarik(1000000, "123456")

    try:
        rek.saldo = -50000
    except ValueError as err:
        print(f"\nValidasi Tertangkap: {err}")

    print("\n--- Uji Proteksi Private Attribute ---")
    try:
        print(rek.__saldo)
    except AttributeError:
        print("Akses langsung rek.__saldo GAGAL karena terlindungi (AttributeError)!")
    print("Nilai via Name Mangling (rek._RekeningBank__saldo): Rp", rek._RekeningBank__saldo)
    rek.cetak_mutasi()
