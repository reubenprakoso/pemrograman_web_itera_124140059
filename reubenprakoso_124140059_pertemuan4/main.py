"""
Program utama untuk menguji seluruh fungsi dari math_operations.py.
"""

# Cara impor pertama: mengimpor modul, lalu memanggil fungsi melalui nama modul.
import math_operations

# Cara impor kedua: mengimpor fungsi dan konstanta tertentu secara langsung.
from math_operations import (
    PI,
    luas_persegi,
    keliling_persegi,
    celsius_ke_fahrenheit,
    celsius_ke_kelvin,
)


def main():
    """Menjalankan contoh perhitungan geometri dan konversi temperatur."""
    print("=" * 55)
    print("             PROGRAM MATEMATIKA PYTHON")
    print("=" * 55)

    sisi = 5
    panjang = 8
    lebar = 4
    jari_jari = 7

    print("\n--- PERSEGI ---")
    print(f"Sisi              : {sisi}")
    print(f"Luas              : {luas_persegi(sisi):.2f}")
    print(f"Keliling          : {keliling_persegi(sisi):.2f}")

    print("\n--- PERSEGI PANJANG ---")
    print(f"Panjang dan lebar : {panjang} x {lebar}")
    print(
        "Luas              : "
        f"{math_operations.luas_persegi_panjang(panjang, lebar):.2f}"
    )
    print(
        "Keliling          : "
        f"{math_operations.keliling_persegi_panjang(panjang, lebar):.2f}"
    )

    print("\n--- LINGKARAN ---")
    print(f"Jari-jari         : {jari_jari}")
    print(f"Konstanta PI      : {PI}")
    print(
        "Luas              : "
        f"{math_operations.luas_lingkaran(jari_jari):.2f}"
    )
    print(
        "Keliling          : "
        f"{math_operations.keliling_lingkaran(jari_jari):.2f}"
    )

    suhu_celsius = 30
    print("\n--- KONVERSI SUHU ---")
    print(f"Celsius           : {suhu_celsius:.2f} °C")
    print(f"Fahrenheit        : {celsius_ke_fahrenheit(suhu_celsius):.2f} °F")
    print(f"Kelvin            : {celsius_ke_kelvin(suhu_celsius):.2f} K")


if __name__ == "__main__":
    main()
