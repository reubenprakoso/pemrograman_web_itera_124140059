"""Pengelolaan koleksi, pencarian, dan peminjaman item perpustakaan."""

from library_item import LibraryItem
from member import Member


class Library:
    """Menyimpan koleksi item secara private dan menyediakan operasi katalog."""

    def __init__(self, nama: str):
        if not nama.strip():
            raise ValueError("Nama perpustakaan wajib diisi.")
        self.nama = nama.strip()
        self.__koleksi: dict[str, LibraryItem] = {}

    def tambah_item(self, item: LibraryItem) -> None:
        """Menambahkan item jika bertipe valid dan ID-nya belum digunakan."""
        if not isinstance(item, LibraryItem):
            raise TypeError("Item yang ditambahkan harus merupakan LibraryItem.")
        if item.item_id in self.__koleksi:
            raise ValueError(f"ID item '{item.item_id}' sudah digunakan.")
        self.__koleksi[item.item_id] = item
        print(f"Item '{item.judul}' berhasil ditambahkan ke {self.nama}.")

    def daftar_item(self) -> tuple[LibraryItem, ...]:
        """Mengembalikan snapshot immutable dari seluruh koleksi."""
        return tuple(self.__koleksi.values())

    def tampilkan_katalog(self) -> list[LibraryItem]:
        """Menampilkan dan mengembalikan item yang saat ini tersedia."""
        tersedia = [item for item in self.__koleksi.values() if not item.is_dipinjam]
        print(f"\n=== Katalog Tersedia: {self.nama} ===")
        if not tersedia:
            print("Tidak ada item yang tersedia.")
        for item in tersedia:
            # Polymorphism: tiap subclass menghasilkan detailnya sendiri.
            print(item.get_detail())
        return tersedia

    def cari_item(self, kata_kunci: str) -> list[LibraryItem]:
        """Mencari berdasarkan ID persis atau judul yang cocok sebagian."""
        query = kata_kunci.strip().casefold()
        if not query:
            return []
        return [
            item
            for item in self.__koleksi.values()
            if item.item_id.casefold() == query or query in item.judul.casefold()
        ]

    def pinjam_item(self, item_id: str, member: Member) -> bool:
        """Meminjamkan item yang tersedia dan mencatatnya ke anggota."""
        if not isinstance(member, Member):
            raise TypeError("Peminjam harus merupakan objek Member.")
        item = self.__koleksi.get(item_id)
        if item is None:
            print(f"Item dengan ID '{item_id}' tidak ditemukan.")
            return False
        if item.is_dipinjam:
            print(f"Item '{item.judul}' sedang tidak tersedia.")
            return False
        item._pinjam(member.member_id)
        member._catat_peminjaman(item.item_id)
        print(f"{member.nama} berhasil meminjam '{item.judul}'.")
        return True

    def kembalikan_item(self, item_id: str, member: Member) -> bool:
        """Menerima pengembalian hanya dari anggota yang meminjam item."""
        if not isinstance(member, Member):
            raise TypeError("Pengembali harus merupakan objek Member.")
        item = self.__koleksi.get(item_id)
        if item is None:
            print(f"Item dengan ID '{item_id}' tidak ditemukan.")
            return False
        if not item.is_dipinjam or item.borrower_id != member.member_id:
            print(f"{member.nama} tidak tercatat sebagai peminjam '{item.judul}'.")
            return False
        item._kembalikan()
        member._hapus_peminjaman(item.item_id)
        print(f"'{item.judul}' berhasil dikembalikan oleh {member.nama}.")
        return True
