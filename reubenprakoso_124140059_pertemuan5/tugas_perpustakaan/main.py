"""Demo fitur sistem manajemen perpustakaan."""

from library import Library
from library_item import Book, Magazine
from member import Member


def main() -> None:
    """Mendemonstrasikan penambahan, katalog, pencarian, dan peminjaman."""
    perpustakaan = Library("Perpustakaan ITERA")
    perpustakaan.tambah_item(Book("B001", "Belajar Python", "Guido van Rossum", 350))
    perpustakaan.tambah_item(Book("B002", "Clean Code", "Robert C. Martin", 464))
    perpustakaan.tambah_item(
        Magazine("M001", "Teknologi Masa Kini", "Edisi 12", "Media Sains")
    )

    perpustakaan.tampilkan_katalog()

    print("\n=== Pencarian Judul: 'python' ===")
    for item in perpustakaan.cari_item("python"):
        print(item.get_detail())

    print("\n=== Pencarian ID: B002 ===")
    for item in perpustakaan.cari_item("B002"):
        print(item.get_detail())

    anggota = Member("A001", "Reuben Prakoso")
    print(f"\n=== Peminjaman oleh {anggota} ===")
    anggota.pinjam(perpustakaan, "B001")
    print(
        "Status dipinjam via property:", perpustakaan.cari_item("B001")[0].is_dipinjam
    )
    print("Koleksi anggota:", anggota.item_dipinjam)

    perpustakaan.tampilkan_katalog()
    print("\n=== Pengembalian ===")
    anggota.kembalikan(perpustakaan, "B001")
    perpustakaan.tampilkan_katalog()

    buku = perpustakaan.cari_item("B001")[0]
    majalah = perpustakaan.cari_item("M001")[0]
    print("\nDenda buku terlambat 3 hari : Rp", f"{buku.hitung_denda(3):,.0f}")
    print("Denda majalah terlambat 3 hari: Rp", f"{majalah.hitung_denda(3):,.0f}")


if __name__ == "__main__":
    main()
