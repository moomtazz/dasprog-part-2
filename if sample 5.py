# Input oleh pengguna
penggunaan_data = float(input("Masukkan penggunaan data (Gb): "))

biaya = 0

# Hitung biaya berdasarkan penggunaan data
if 0.0 < penggunaan_data <= 1.0:
    biaya = 250
elif 1.0 < penggunaan_data <= 2.0:
    biaya = 500
elif 2.0 < penggunaan_data <= 5.0:
    biaya = 1000
elif 5.0 < penggunaan_data <= 10.0:
    biaya = 1500
elif penggunaan_data > 10.0:
    biaya = 2000
else:
    print("Data tidak valid.")

# Tampilkan hasil biaya
if biaya > 0:
    print(f"Biaya yang harus dibayar: Rp {biaya}")
