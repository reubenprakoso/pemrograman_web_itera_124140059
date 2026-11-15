"""Contoh polymorphism, duck typing, dan operator overloading."""


class MetodePembayaran:
    """Superclass metode pembayaran dengan antarmuka bayar."""

    def __init__(self, nama_metode: str):
        self.nama_metode = nama_metode

    def bayar(self, tagihan: float) -> bool:
        raise NotImplementedError("Subclass wajib mengimplementasikan method bayar()!")


class TransferBank(MetodePembayaran):
    """Pembayaran melalui transfer virtual account."""

    def __init__(self, nama_bank: str, nomor_va: str):
        super().__init__(f"Transfer Bank {nama_bank}")
        self.nomor_va = nomor_va

    def bayar(self, tagihan: float) -> bool:
        biaya_admin = 4000
        total = tagihan + biaya_admin
        print(
            f"[{self.nama_metode}] Tagihan: Rp {tagihan:,.2f} + Admin: Rp {biaya_admin:,} = Total: Rp {total:,.2f}"
        )
        print(f" -> Silakan transfer tepat ke Virtual Account: {self.nomor_va}")
        return True


class EWallet(MetodePembayaran):
    """Pembayaran e-wallet dengan saldo dan promo cashback."""

    def __init__(self, nama_provider: str, nomor_hp: str, saldo_wallet: float):
        super().__init__(f"E-Wallet {nama_provider}")
        self.nomor_hp = nomor_hp
        self.saldo_wallet = saldo_wallet

    def bayar(self, tagihan: float) -> bool:
        if tagihan <= 0:
            print("Tagihan harus lebih besar dari Rp 0.")
            return False
        cashback = tagihan * 0.05
        if self.saldo_wallet < tagihan:
            print(
                f"[{self.nama_metode}] Gagal: Saldo e-wallet tidak cukup! (Saldo: Rp {self.saldo_wallet:,.2f})"
            )
            return False
        self.saldo_wallet -= tagihan
        print(
            f"[{self.nama_metode}] Pembayaran Rp {tagihan:,.2f} BERHASIL via akun {self.nomor_hp}."
        )
        print(
            f" -> Selamat! Anda mendapatkan cashback Rp {cashback:,.2f}. Sisa saldo: Rp {self.saldo_wallet:,.2f}"
        )
        return True


class CryptoPayment:
    """Gateway crypto yang mendemonstrasikan duck typing tanpa inheritance."""

    def __init__(self, wallet_address: str, crypto_symbol: str = "USDT"):
        self.wallet_address = wallet_address
        self.crypto_symbol = crypto_symbol

    def bayar(self, tagihan: float) -> bool:
        if tagihan <= 0:
            print("Tagihan harus lebih besar dari Rp 0.")
            return False
        total_crypto = tagihan / 16000
        print(
            f"[Crypto Gateway] Mengonversi Rp {tagihan:,.2f} -> {total_crypto:.2f} {self.crypto_symbol}"
        )
        print(
            f" -> Transaksi tercatat untuk wallet {self.wallet_address[:10]}... Success!"
        )
        return True


def proses_checkout_pesanan(daftar_opsi_bayar: list, total_belanja: float) -> None:
    """Memanggil method bayar pada setiap objek dengan duck typing."""
    print(
        f"\n================ PROSES CHECKOUT TAGIHAN Rp {total_belanja:,.2f} ================"
    )
    for opsi in daftar_opsi_bayar:
        nama = getattr(opsi, "nama_metode", type(opsi).__name__)
        print(f"\nMemproses opsi: {nama}...")
        opsi.bayar(total_belanja)


class Dompet:
    """Dompet sederhana dengan dukungan operator + dan ==."""

    def __init__(self, pemilik: str, saldo: float):
        self.pemilik = pemilik
        self.saldo = saldo

    def __add__(self, other):
        if isinstance(other, Dompet):
            return Dompet(f"{self.pemilik} & {other.pemilik}", self.saldo + other.saldo)
        if isinstance(other, (int, float)) and not isinstance(other, bool):
            return Dompet(self.pemilik, self.saldo + other)
        return NotImplemented

    def __eq__(self, other) -> bool:
        if isinstance(other, Dompet):
            return self.saldo == other.saldo
        return NotImplemented

    def __str__(self) -> str:
        return f"Dompet({self.pemilik}): Rp {self.saldo:,.2f}"


if __name__ == "__main__":
    va_bca = TransferBank("BCA", "880121140001")
    gopay = EWallet("GoPay", "081234567890", saldo_wallet=500000)
    crypto = CryptoPayment("0x71C...b89A", "USDT")
    proses_checkout_pesanan([va_bca, gopay, crypto], 320000)

    print("\n--- Uji Operator Overloading Dompet ---")
    d1 = Dompet("Andi", 150000)
    d2 = Dompet("Budi", 250000)
    print("Dompet 1 :", d1)
    print("Dompet 2 :", d2)
    print("Hasil d1 + d2 :", d1 + d2)
    print("Apakah saldo d1 == d2? :", d1 == d2)
