"""Latihan mandiri polymorphism untuk broadcast berbagai kanal notifikasi."""


class NotifikasiEmail:
    """Kanal pengiriman notifikasi melalui email."""

    def kirim(self, pesan: str, penerima: str) -> None:
        print(f"[Email] Kepada {penerima}: {pesan}")


class NotifikasiSMS:
    """Kanal pengiriman notifikasi melalui SMS."""

    def kirim(self, pesan: str, penerima: str) -> None:
        print(f"[SMS] Ke {penerima}: {pesan}")


class NotifikasiWhatsApp:
    """Kanal pengiriman notifikasi melalui WhatsApp."""

    def kirim(self, pesan: str, penerima: str) -> None:
        print(f"[WhatsApp] Ke {penerima}: {pesan}")


def broadcast_pengumuman(daftar_channel: list[tuple[object, str]], pesan: str) -> None:
    """Mengirim pesan ke setiap pasangan kanal dan alamat penerimanya."""
    for channel, penerima in daftar_channel:
        channel.kirim(pesan, penerima)


if __name__ == "__main__":
    kanal = [
        (NotifikasiEmail(), "mahasiswa@itera.ac.id"),
        (NotifikasiSMS(), "+6281234567890"),
        (NotifikasiWhatsApp(), "+6281234567890"),
    ]
    broadcast_pengumuman(kanal, "Pengumuman darurat: praktikum dimulai pukul 13.00.")
