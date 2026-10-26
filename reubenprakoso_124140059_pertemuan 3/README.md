# Manajemen Buku Pribadi

## 1. Deskripsi Aplikasi

Manajemen Buku Pribadi adalah aplikasi berbasis web yang dibuat menggunakan React untuk membantu pengguna mencatat dan mengelola koleksi buku. Pengguna dapat menambahkan buku, mengubah informasi buku, menghapus buku, mencari buku, dan melihat statistik koleksi buku.

## 2. Fitur Aplikasi

- Menambahkan buku dengan judul, nama penulis, dan status kepemilikan.
- Mengedit informasi buku.
- Menghapus buku dari daftar.
- Mencari buku berdasarkan judul atau nama penulis.
- Memfilter buku berdasarkan status.
- Menampilkan statistik koleksi buku.
- Menyimpan data buku menggunakan localStorage agar tetap tersedia ketika halaman dimuat kembali.
- Memvalidasi input agar judul dan nama penulis tidak kosong.

## 3. Teknologi yang Digunakan

- **React** — membangun antarmuka aplikasi.
- **Vite** — menjalankan lingkungan pengembangan.
- **React Router DOM** — mengatur navigasi halaman.
- **Context API** — membagikan dan mengelola data buku.
- **Custom Hooks** — memisahkan logika penyimpanan dan perhitungan statistik.
- **PropTypes** — memvalidasi tipe props komponen.
- **localStorage** — menyimpan data buku pada browser.
- **Vitest** — menjalankan pengujian otomatis.
- **React Testing Library** — menguji komponen React.

## 4. Struktur Folder

- `src/components/BookForm/` — formulir penambahan buku.
- `src/components/BookList/` — menampilkan, mengedit, dan menghapus buku.
- `src/components/BookFilter/` — pencarian dan filter buku.
- `src/context/BookContext.jsx` — pengelolaan data buku menggunakan Context API.
- `src/hooks/useLocalStorage.js` — custom hook untuk penyimpanan data.
- `src/hooks/useBookStats.js` — custom hook untuk menghitung statistik buku.
- `src/pages/Home/Home.jsx` — halaman utama aplikasi.
- `src/pages/Stats/Stats.jsx` — halaman statistik koleksi buku.
- `src/test/BookForm.test.jsx` — pengujian komponen formulir buku.

## 5. Cara Menjalankan Aplikasi

Pastikan Node.js dan npm telah terpasang pada komputer.

1. Buka terminal di folder proyek.
2. Jalankan perintah berikut untuk memasang dependensi:

   ```bash
   npm install
   ```

3. Jalankan aplikasi:

   ```bash
   npm run dev
   ```

4. Buka alamat lokal yang ditampilkan pada terminal di browser.

## 6. Cara Menjalankan Pengujian

Jalankan perintah berikut di terminal:

```bash
npm run test -- --run
```

Pengujian dilakukan menggunakan Vitest dan React Testing Library untuk memeriksa fungsi formulir penambahan buku.

## 7. Hasil Pengujian

File `src/test/BookForm.test.jsx` berisi lima pengujian:

1. Memastikan formulir penambahan buku ditampilkan.
2. Memastikan pesan validasi muncul ketika judul dan penulis kosong.
3. Memastikan data buku dikirim ketika formulir diisi dengan benar.
4. Memastikan status buku default adalah Sudah Dimiliki.
5. Memastikan formulir dikosongkan setelah buku berhasil ditambahkan.

Hasil pengujian terakhir menunjukkan **5 pengujian berhasil**.

## 8. Identitas Mahasiswa

- **Nama:** Reuben Prakoso
- **NIM:** 124140059
- **Mata Kuliah:** Pemrograman Aplikasi Web (PAW)
- **Tugas:** Praktikum Pertemuan 3