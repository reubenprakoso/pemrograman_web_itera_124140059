"""Abstract item perpustakaan serta implementasi buku dan majalah."""

from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """Base class item perpustakaan dengan status peminjaman terlindungi."""

    def __init__(self, item_id: str, judul: str):
        if not item_id.strip() or not judul.strip():
            raise ValueError("ID dan judul item wajib diisi.")
        self.__item_id = item_id.strip()
        self.__judul = judul.strip()
        self._dipinjam = False
        self._borrower_id: str | None = None

    @property
    def item_id(self) -> str:
        """ID unik item yang hanya dapat dibaca dari luar."""
        return self.__item_id

    @property
    def judul(self) -> str:
        """Judul item yang hanya dapat dibaca dari luar."""
        return self.__judul

    @property
    def is_dipinjam(self) -> bool:
        """Status peminjaman item yang dibaca melalui property."""
        return self._dipinjam

    @property
    def borrower_id(self) -> str | None:
        """ID peminjam saat ini, jika item sedang dipinjam."""
        return self._borrower_id

    def _pinjam(self, member_id: str) -> None:
        """Mengubah status item menjadi dipinjam; dipanggil oleh Library."""
        if self._dipinjam:
            raise ValueError(f"Item '{self.item_id}' sedang dipinjam.")
        self._dipinjam = True
        self._borrower_id = member_id

    def _kembalikan(self) -> None:
        """Mengubah status item menjadi tersedia; dipanggil oleh Library."""
        self._dipinjam = False
        self._borrower_id = None

    @abstractmethod
    def get_detail(self) -> str:
        """Menghasilkan detail item; wajib didefinisikan subclass."""
        raise NotImplementedError

    @abstractmethod
    def hitung_denda(self, hari_terlambat: int) -> float:
        """Menghitung denda item untuk jumlah hari keterlambatan."""
        raise NotImplementedError


class Book(LibraryItem):
    """Item buku dengan informasi penulis dan jumlah halaman."""

    DENDA_PER_HARI = 1_000

    def __init__(self, item_id: str, judul: str, penulis: str, jumlah_halaman: int):
        super().__init__(item_id, judul)
        if not penulis.strip() or jumlah_halaman <= 0:
            raise ValueError("Penulis wajib diisi dan jumlah halaman harus positif.")
        self.penulis = penulis.strip()
        self.jumlah_halaman = jumlah_halaman

    def get_detail(self) -> str:
        """Mengembalikan detail lengkap buku untuk katalog."""
        status = "Dipinjam" if self.is_dipinjam else "Tersedia"
        return (
            f"Buku | ID: {self.item_id} | Judul: {self.judul} | "
            f"Penulis: {self.penulis} | {self.jumlah_halaman} halaman | Status: {status}"
        )

    def hitung_denda(self, hari_terlambat: int) -> float:
        """Menghitung denda buku sebesar Rp1.000 per hari."""
        if hari_terlambat < 0:
            raise ValueError("Hari keterlambatan tidak boleh negatif.")
        return hari_terlambat * self.DENDA_PER_HARI


class Magazine(LibraryItem):
    """Item majalah dengan nomor edisi dan nama penerbit."""

    DENDA_PER_HARI = 500

    def __init__(self, item_id: str, judul: str, nomor_edisi: str, penerbit: str):
        super().__init__(item_id, judul)
        if not nomor_edisi.strip() or not penerbit.strip():
            raise ValueError("Nomor edisi dan penerbit wajib diisi.")
        self.nomor_edisi = nomor_edisi.strip()
        self.penerbit = penerbit.strip()

    def get_detail(self) -> str:
        """Mengembalikan detail lengkap majalah untuk katalog."""
        status = "Dipinjam" if self.is_dipinjam else "Tersedia"
        return (
            f"Majalah | ID: {self.item_id} | Judul: {self.judul} | "
            f"Edisi: {self.nomor_edisi} | Penerbit: {self.penerbit} | Status: {status}"
        )

    def hitung_denda(self, hari_terlambat: int) -> float:
        """Menghitung denda majalah sebesar Rp500 per hari."""
        if hari_terlambat < 0:
            raise ValueError("Hari keterlambatan tidak boleh negatif.")
        return hari_terlambat * self.DENDA_PER_HARI
