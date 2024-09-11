#program untuk mengetahui suhu dalam freezer

#input data
jam = int(input("masukkan jumlah jam setelah freezer mati:"))
menit = int(input("masukkan jumlah menit setelah freezer mati:"))

#mengonversi waktu yang telah berlalu menjadi jam
waktu_total = jam + (menit/60)

#menghitung suhu menggunakan rumus
suhu = (4*waktu_total**2)/(waktu_total+2)-20

#hasil suhu
print(f"suhu freezer anda saat ini adalah: {suhu:.2f} derajat Celcius")