"""Model anggota perpustakaan."""


class Member:
    """Anggota dengan daftar pinjaman yang dikelola melalui metode."""

    def __init__(self, member_id: str, nama: str):
        if not member_id.strip() or not nama.strip():
            raise ValueError("ID anggota dan nama wajib diisi.")
        self.__member_id = member_id.strip()
        self.__nama = nama.strip()
        self.__item_dipinjam: set[str] = set()

    @property
    def member_id(self) -> str:
        """ID anggota yang hanya dapat dibaca."""
        return self.__member_id

    @property
    def nama(self) -> str:
        """Nama anggota yang hanya dapat dibaca."""
        return self.__nama

    @property
    def item_dipinjam(self) -> tuple[str, ...]:
        """Salinan immutable ID item yang sedang dipinjam anggota."""
        return tuple(sorted(self.__item_dipinjam))

    def pinjam(self, library, item_id: str) -> bool:
        """Meminta Library meminjamkan item kepada anggota ini."""
        return library.pinjam_item(item_id, self)

    def kembalikan(self, library, item_id: str) -> bool:
        """Meminta Library memproses pengembalian item anggota ini."""
        return library.kembalikan_item(item_id, self)

    def _catat_peminjaman(self, item_id: str) -> None:
        """Mencatat pinjaman setelah Library berhasil memvalidasinya."""
        self.__item_dipinjam.add(item_id)

    def _hapus_peminjaman(self, item_id: str) -> None:
        """Menghapus catatan pinjaman setelah item berhasil dikembalikan."""
        self.__item_dipinjam.discard(item_id)

    def __str__(self) -> str:
        return f"{self.nama} (ID: {self.member_id})"
