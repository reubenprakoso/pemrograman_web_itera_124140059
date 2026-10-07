# Tugas Praktikum PAW Pertemuan 1 - Kasir Mini POS

## Identitas
- **Nama**: Reuben Prakoso
- **NIM**: 124140059
- **Kelas Praktikum**: RA 

## Deskripsi Aplikasi
Aplikasi Kasir & Keranjang Belanja Sederhana (Mini POS) adalah aplikasi berbasis web yang dirancang untuk mengelola transaksi kasir di kantin atau toko kampus. Aplikasi ini mengintegrasikan tiga fitur utama:
1. Validasi input form interaktif untuk mencegah masukan data yang keliru.
2. Perhitungan matematis otomatis (Subtotal, Accumulative Total, Diskon Otomatis 10%, dan Uang Kembalian).
3. Manajemen state persisten menggunakan `localStorage` browser.

## Panduan Menjalankan Aplikasi
1. Clone atau unduh repository GitHub proyek: `https://github.com/[username]/pemrograman_web_itera_124140059`.
2. Buka folder `reubenprakoso_124140059_pertemuan1` menggunakan editor Visual Studio Code.
3. Jalankan file `index.html` menggunakan ekstensi **Live Server** di Visual Studio Code, atau buka file `index.html` secara langsung pada browser favorit Anda.

## Daftar Fitur Utama
- [x] **Validasi Form Input**: Nama barang min. 3 karakter, harga satuan min. Rp 500, dan Qty min. 1.
- [x] **Perhitungan Otomatis**: Subtotal per baris, Total akumulasi, Diskon 10% (otomatis saat total ≥ Rp 50.000 atau menggunakan kode kupon `HEMAT10`).
- [x] **Kalkulator Uang Kembalian**: Menghitung selisih pembayaran dan memberikan indikasi jika nominal pembayaran kurang.
- [x] **Manajemen Keranjang Belanja**: Menambah dan menghapus barang dari keranjang secara responsif.
- [x] **Persistensi Data (LocalStorage)**: Menyimpan dan memuat state keranjang belanja dengan JSON serialization (`JSON.stringify` dan `JSON.parse`).
- [x] **Reset Transaksi**: Mengosongkan keranjang dan menghapus data dari localStorage.

## Penjelasan Teknis Singkat
1. **Validasi Form**: Fungsi `validateForm()` memeriksa kriteria teks dan batas nilai menggunakan manipulasi String dan kriteria tipe data number. Jika ditemukan kesalahan, pesan error dinamis dirender ke elemen HTML `<small class="error-msg">`.
2. **Kalkulasi Keuangan**: Fungsi `hitungKalkulasi()` memanfaatkan metode Array ES6 `reduce()` untuk mengakumulasi total belanja, lalu mengevaluasi klausa kondisional diskon sebelum menghasilkan nominal `totalAkhir`.
3. **Serialisasi LocalStorage**: Setiap perubahan pada array JavaScript `keranjang` memicu pemanggilan `saveToLocalStorage()`, yang mengonversi array objek ke string JSON melalui `JSON.stringify()`. Saat aplikasi dimuat pertama kali (`DOMContentLoaded`), fungsi `initApp()` memulihkan array dari `localStorage` via `JSON.parse()`.