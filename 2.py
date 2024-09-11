#program menghitung VTBI dan laju infus dalam ml/jam

#input jumlah cairan dalam kantong (ml)
jumlah_cairan = int(input("masukkan jumlah cairan dalam kantong (ml): "))

#input waktu infus (menit)
waktu_infus = int(input("waktu infus (menit): "))

#menghitung laju infus (ml/jam)
laju_infus = (jumlah_cairan/waktu_infus)*60

#hasil
print(f"VTBI:{jumlah_cairan} ml")
print(f"laju_infus:{laju_infus} ml/jam")