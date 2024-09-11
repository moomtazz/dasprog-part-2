#Program untuk menghitung jumlah bagian yang dibutuhkan berdasarkan siswa yang terdaftar

#memasukkan jumlah siswa
jumlah_siswa = int(input("jumlah siswa yang terdaftar: "))

#kapasitas setiap bagian
kapasitas = 30 #siswa

#menghitung jumlah bagian yang dibutuhkan
jumlah_bagian = jumlah_siswa // kapasitas

#menghitung sisa siswa yang tidak masuk bagian
sisa_siswa = jumlah_siswa % kapasitas

#hasil
print ("jumlah siswa yang terdaftar:", jumlah_siswa)
print ("jumlah bagian yang dibutuhkan:", jumlah_bagian)
print ("jumlah siswa yang tidak mendapat bagian:", sisa_siswa)