"""
Program penghitung BMI (Body Mass Index).

Pengguna memasukkan berat badan dalam kilogram dan tinggi badan
dalam meter. Program menghitung BMI dan menampilkan kategorinya.
"""

berat_badan = float(input("Masukkan berat badan (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan (m): "))

if berat_badan <= 0 or tinggi_badan <= 0:
    print("Berat badan dan tinggi badan harus lebih dari 0.")
else:
    bmi = berat_badan / (tinggi_badan * tinggi_badan)

    if bmi < 18.5:
        kategori = "Berat badan kurang"
    elif bmi < 25:
        kategori = "Berat badan normal"
    elif bmi < 30:
        kategori = "Berat badan berlebih"
    else:
        kategori = "Obesitas"

    print("\n=== HASIL PERHITUNGAN BMI ===")
    print(f"Berat badan : {berat_badan:.2f} kg")
    print(f"Tinggi badan: {tinggi_badan:.2f} m")
    print(f"Nilai BMI   : {bmi:.2f}")
    print(f"Kategori    : {kategori}")
