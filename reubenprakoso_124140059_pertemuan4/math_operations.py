"""
Modul fungsi matematika untuk geometri dan konversi suhu.
"""

PI = 3.14159


def luas_persegi(sisi):
    """Menerima panjang sisi dan mengembalikan luas persegi."""
    return sisi * sisi


def keliling_persegi(sisi):
    """Menerima panjang sisi dan mengembalikan keliling persegi."""
    return 4 * sisi


def luas_persegi_panjang(panjang, lebar):
    """Menerima panjang dan lebar, lalu mengembalikan luas persegi panjang."""
    return panjang * lebar


def keliling_persegi_panjang(panjang, lebar):
    """Menerima panjang dan lebar, lalu mengembalikan keliling persegi panjang."""
    return 2 * (panjang + lebar)


def luas_lingkaran(jari_jari):
    """Menerima jari-jari dan mengembalikan luas lingkaran."""
    return PI * jari_jari ** 2


def keliling_lingkaran(jari_jari):
    """Menerima jari-jari dan mengembalikan keliling lingkaran."""
    return 2 * PI * jari_jari


def celsius_ke_fahrenheit(celsius):
    """Menerima suhu Celsius dan mengembalikan hasil konversi Fahrenheit."""
    return (celsius * 9 / 5) + 32


def celsius_ke_kelvin(celsius):
    """Menerima suhu Celsius dan mengembalikan hasil konversi Kelvin."""
    return celsius + 273.15
