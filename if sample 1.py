#program untuk menghitung diskon dan pajak

#input oleh pengguna
total_awal = float(input("masukkan total pembelian anda:"))
siswa = input("apakah anda siswa? (ya/tidak):")

#diskon
if (siswa == 'ya'):
   diskon_siswa = total_awal-(0.2*total_awal)
   pajak_siswa = diskon_siswa+(0.05*diskon_siswa)
   print(f"total yang harus anda bayar adalah: {pajak_siswa}")
else:
    pajak_nonsiswa = total_awal+(0.05*total_awal)
    print(f"total yang harus anda bayar adalah: {pajak_nonsiswa}")