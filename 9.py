#Program menghitung waktu dalam memotong rumput di halaman

#input data 
Panjang_Halaman = float(input("Masukkan panjang halaman (dalam kaki): "))
Lebar_Halaman = float(input("Masukkan lebar halaman (dalam kaki): "))
Panjang_Rumah = float(input("Masukkan panjang rumah (dalam kaki): "))
Lebar_Rumah = float(input("Masukkan lebar rumah (dalam kaki): "))

#Menghitung area rumput yang akan dipotong
Luas_Halaman = Panjang_Halaman * Lebar_Halaman
Luas_Rumah = Panjang_Rumah * Lebar_Rumah
Halaman_Rumput = Luas_Halaman - Luas_Rumah

#kecepatan memotong rumput
Kecepatan_Pemotongan = 2 #kaki persegi per detik

#Menghitung waktu pemotongan
waktu_pemotongan = Halaman_Rumput / Kecepatan_Pemotongan

#Waktu dalam memotong rumput
print(f"Waktu yang dibutuhkan untuk memotong rumput: {waktu_pemotongan} detik")