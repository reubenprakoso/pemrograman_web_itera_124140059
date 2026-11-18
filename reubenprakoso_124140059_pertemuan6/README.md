# Praktikum Pengembangan Aplikasi Web — Pertemuan 6

## Identitas

- **Nama:** Reuben Prakoso
- **NIM:** 124140059
- **Kelas Praktikum:** RA
- **Program Studi:** Teknik Informatika

## Deskripsi

Aplikasi RESTful API berbasis Pyramid untuk mengelola data Mahasiswa dan
Matakuliah. SQLAlchemy digunakan sebagai ORM, PostgreSQL sebagai database,
Alembic untuk migrasi, dan `pyramid_tm` untuk mengelola transaksi per request.

Endpoint tersedia di `/api/mahasiswa` dan `/api/matakuliah` dengan operasi
`GET` daftar/detail, `POST`, `PUT`, dan `DELETE`. Validasi memastikan field
wajib terisi, kode/NIM unik, serta SKS dan semester merupakan integer positif.

## Persyaratan

- Python 3.10 atau lebih baru
- PostgreSQL 13 atau lebih baru
- `psql` dan `curl.exe` (untuk pengujian endpoint di Windows)

## Instalasi di Windows PowerShell

Jalankan dari direktori `reubenprakoso_124140059_pertemuan6`:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[testing]"
```

Jika PowerShell memblokir aktivasi script, gunakan Command Prompt dengan
`venv\Scripts\activate.bat`, atau atur execution policy untuk akun Anda.
Jika `pip install` gagal karena batas panjang path Windows, buat virtual
environment di lokasi yang lebih pendek, misalnya `C:\p6env`, lalu aktifkan
`C:\p6env\Scripts\Activate.ps1` dan ulangi instalasi dari direktori proyek.

## Menyiapkan PostgreSQL

Masuk ke `psql` sebagai administrator PostgreSQL, lalu jalankan:

```sql
CREATE DATABASE pyramid_mahasiswa;
CREATE USER pyramid_user WITH ENCRYPTED PASSWORD 'pyramid_pass';
GRANT ALL PRIVILEGES ON DATABASE pyramid_mahasiswa TO pyramid_user;
\c pyramid_mahasiswa
GRANT ALL ON SCHEMA public TO pyramid_user;
```

Kredensial pada `development.ini` adalah contoh untuk database lokal praktikum.
Jangan gunakan kredensial tersebut di server publik. Untuk mengganti URL koneksi
pada sesi PowerShell saat ini:

```powershell
$env:DATABASE_URL = "postgresql+psycopg2://pyramid_user:pyramid_pass@localhost:5432/pyramid_mahasiswa"
```

## Migrasi, seeding, dan menjalankan server

Jalankan semua perintah dari direktori proyek yang berisi `development.ini`:

```powershell
alembic -c development.ini upgrade head
python -m pyramid_mahasiswa.scripts.initialize_db development.ini
pserve development.ini --reload
```

Migrasi `0001` membuat tabel mahasiswa dan migrasi `0002` membuat tabel
matakuliah beserta unique index dan constraint positif untuk SKS/semester.
Seeding aman dijalankan berulang kali dan menambahkan dua mahasiswa serta tiga
mata kuliah contoh.

## Pengujian API

Biarkan server berjalan pada `http://127.0.0.1:6543`. Untuk menjalankan seluruh
skenario CRUD dan validasi secara berurutan dari PowerShell, gunakan skrip:

```powershell
.\test_api.ps1 -Resource mahasiswa
.\test_api.ps1 -Resource matakuliah
```

Skrip menampilkan setiap status HTTP dan respons JSON, serta menghapus record
uji yang dibuatnya. Ambil screenshot output aktual untuk kedua resource.
Perintah `curl.exe` manual di bawah tetap dapat digunakan untuk pengujian satu per satu.

### Mahasiswa

```powershell
curl.exe http://127.0.0.1:6543/api/mahasiswa
curl.exe http://127.0.0.1:6543/api/mahasiswa/1
curl.exe -X POST http://127.0.0.1:6543/api/mahasiswa -H "Content-Type: application/json" -d '{"nim":"124140099","nama":"Dewi Lestari","jurusan":"Teknik Informatika","tanggal_lahir":"2002-06-10","alamat":"Bandar Lampung"}'
curl.exe -X PUT http://127.0.0.1:6543/api/mahasiswa/1 -H "Content-Type: application/json" -d '{"jurusan":"Teknik Informatika"}'
curl.exe -X DELETE http://127.0.0.1:6543/api/mahasiswa/3
```

### Matakuliah

```powershell
curl.exe http://127.0.0.1:6543/api/matakuliah
curl.exe http://127.0.0.1:6543/api/matakuliah/1
curl.exe -X POST http://127.0.0.1:6543/api/matakuliah -H "Content-Type: application/json" -d '{"kode_mk":"IF3140","nama_mk":"Basis Data","sks":4,"semester":5}'
curl.exe -X PUT http://127.0.0.1:6543/api/matakuliah/1 -H "Content-Type: application/json" -d '{"sks":3,"semester":6}'
curl.exe -X DELETE http://127.0.0.1:6543/api/matakuliah/3
```

Uji validasi (harus mendapat HTTP 400 karena SKS nol):

```powershell
curl.exe -i -X POST http://127.0.0.1:6543/api/matakuliah -H "Content-Type: application/json" -d '{"kode_mk":"IF9999","nama_mk":"Contoh","sks":0,"semester":3}'
```

Jalankan pengujian otomatis dengan SQLite sementara (tidak memerlukan server
PostgreSQL):

```powershell
pytest
```

## Screenshot pengujian

Screenshot aktual pengujian mencakup daftar, detail, tambah, ubah, hapus,
serta validasi dan status HTTP. Simpan empat tangkapan layar terminal berikut
di folder `screenshots/`:

- `screenshots/mahasiswa_api1.png` — daftar, tambah, dan detail mahasiswa.
- `screenshots/mahasiswa_api2.png` — ubah, validasi, hapus, dan respons 404.
- `screenshots/matakuliah_api1.png` — daftar, tambah, dan detail matakuliah.
- `screenshots/matakuliah_api2.png` — ubah, validasi, hapus, dan respons 404.

Gunakan hasil pengujian aktual dari terminal Anda, bukan screenshot contoh.

## Struktur proyek

```text
reubenprakoso_124140059_pertemuan6/
├── .gitignore
├── README.md
├── development.ini
├── production.ini
├── requirements.txt
├── setup.py
├── pytest.ini
├── test_api.ps1
├── screenshots/
├── tests/
│   └── test_api.py
└── pyramid_mahasiswa/
    ├── __init__.py
    ├── routes.py
    ├── alembic/
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions/
    │       ├── 0001_create_mahasiswa.py
    │       └── 0002_create_matakuliah.py
    ├── models/
    │   ├── __init__.py
    │   ├── meta.py
    │   ├── mahasiswa.py
    │   └── matakuliah.py
    ├── scripts/
    │   └── initialize_db.py
    └── views/
        ├── common.py
        ├── default.py
        ├── mahasiswa.py
        └── matakuliah.py
```

Virtual environment, cache Python, file SQLite lokal, dan rahasia `.env`
diabaikan oleh `.gitignore`.
