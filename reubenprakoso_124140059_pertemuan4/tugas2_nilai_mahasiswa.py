"""
Program pengelolaan nilai mahasiswa.

Menghitung nilai akhir dengan bobot UTS 30%, UAS 40%, dan tugas 30%,
menentukan grade, serta menampilkan nilai tertinggi dan terendah.
"""

mahasiswa = [
    {"nama": "Reksa", "nim": "124140101", "nilai_uts": 80, "nilai_uas": 85, "nilai_tugas": 90},
    {"nama": "Sampur", "nim": "124140102", "nilai_uts": 75, "nilai_uas": 80, "nilai_tugas": 85},
    {"nama": "Daffa", "nim": "124140103", "nilai_uts": 60, "nilai_uas": 65, "nilai_tugas": 70},
    {"nama": "Reuben", "nim": "124140104", "nilai_uts": 90, "nilai_uas": 95, "nilai_tugas": 92},
    {"nama": "Abror", "nim": "124140105", "nilai_uts": 50, "nilai_uas": 55, "nilai_tugas": 60},
]


def hitung_nilai_akhir(data):
    """Menghitung nilai akhir dari data mahasiswa; mengembalikan angka nilai."""
    return (
        0.30 * data["nilai_uts"]
        + 0.40 * data["nilai_uas"]
        + 0.30 * data["nilai_tugas"]
    )


def tentukan_grade(nilai_akhir):
    """Menerima nilai akhir dan mengembalikan grade A, B, C, D, atau E."""
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"


for data in mahasiswa:
    data["nilai_akhir"] = hitung_nilai_akhir(data)
    data["grade"] = tentukan_grade(data["nilai_akhir"])

print("=" * 76)
print("                    DAFTAR NILAI MAHASISWA")
print("=" * 76)
print(f"{'Nama':<12}{'NIM':<14}{'UTS':>7}{'UAS':>7}{'Tugas':>8}{'Akhir':>10}{'Grade':>8}")
print("-" * 76)

for data in mahasiswa:
    print(
        f"{data['nama']:<12}{data['nim']:<14}"
        f"{data['nilai_uts']:>7.1f}{data['nilai_uas']:>7.1f}"
        f"{data['nilai_tugas']:>8.1f}{data['nilai_akhir']:>10.2f}"
        f"{data['grade']:>8}"
    )

nilai_tertinggi = max(mahasiswa, key=lambda data: data["nilai_akhir"])
nilai_terendah = min(mahasiswa, key=lambda data: data["nilai_akhir"])

print("-" * 76)
print(
    f"Nilai tertinggi: {nilai_tertinggi['nama']} "
    f"({nilai_tertinggi['nim']}) = {nilai_tertinggi['nilai_akhir']:.2f} "
    f"[{nilai_tertinggi['grade']}]"
)
print(
    f"Nilai terendah : {nilai_terendah['nama']} "
    f"({nilai_terendah['nim']}) = {nilai_terendah['nilai_akhir']:.2f} "
    f"[{nilai_terendah['grade']}]"
)
