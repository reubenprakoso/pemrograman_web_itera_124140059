"""Latihan mandiri abstract class untuk layanan penyimpanan berkas."""

from abc import ABC, abstractmethod


class FileStorage(ABC):
    """Kontrak upload dan download untuk backend penyimpanan berkas."""

    @abstractmethod
    def upload_file(self, nama_file: str, data_bytes: bytes) -> None:
        """Menyimpan data berkas dengan nama tertentu."""
        raise NotImplementedError

    @abstractmethod
    def download_file(self, nama_file: str) -> bytes:
        """Mengambil data berkas berdasarkan namanya."""
        raise NotImplementedError


class LocalDiskStorage(FileStorage):
    """Simulasi penyimpanan lokal di memori, tanpa menulis file sungguhan."""

    def __init__(self):
        self._files: dict[str, bytes] = {}

    def upload_file(self, nama_file: str, data_bytes: bytes) -> None:
        self._files[nama_file] = bytes(data_bytes)
        print(f"[LocalDisk] Berkas '{nama_file}' tersimpan (simulasi).")

    def download_file(self, nama_file: str) -> bytes:
        try:
            return self._files[nama_file]
        except KeyError as err:
            raise FileNotFoundError(
                f"Berkas '{nama_file}' tidak ditemukan di penyimpanan lokal."
            ) from err


class CloudStorage(FileStorage):
    """Simulasi penyimpanan cloud di memori, tanpa koneksi jaringan."""

    def __init__(self):
        self._objects: dict[str, bytes] = {}

    def upload_file(self, nama_file: str, data_bytes: bytes) -> None:
        self._objects[nama_file] = bytes(data_bytes)
        print(f"[Cloud] Berkas '{nama_file}' diunggah (simulasi).")

    def download_file(self, nama_file: str) -> bytes:
        try:
            return self._objects[nama_file]
        except KeyError as err:
            raise FileNotFoundError(
                f"Berkas '{nama_file}' tidak ditemukan di cloud simulasi."
            ) from err


if __name__ == "__main__":
    for storage in (LocalDiskStorage(), CloudStorage()):
        storage.upload_file("catatan.txt", b"Materi OOP Python")
        print("Isi unduhan:", storage.download_file("catatan.txt").decode("utf-8"))
