#Program untuk menghitung tarif taxi berdasarkan jarak tempuh

#tarif setiap mil
tarif_per_mil = 1.50

#input dari pengguna
ordometer_awal = float(input("masukkan ordometer awal:"))
ordometer_akhir = float(input("masukkan ordometer akhir:"))

#menghitung jarak tempuh
jarak_tempuh = ordometer_akhir - ordometer_awal

#menghitung biaya taxi
biaya_taxi = jarak_tempuh*tarif_per_mil

#hasil
print(f"anda menempuh jarak: {jarak_tempuh:.1f} mil")
print(f"biaya taxi anda adalah: {biaya_taxi:.2f} $")