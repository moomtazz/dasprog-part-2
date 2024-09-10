HH, MM, SS = map(int, input().split(':'))
CH, CM, CS = map(int, input().split(':'))

# ubah waktu stream ke GMT+7
HH = HH + 5
# konversi ke detik
waktustreaming = HH * 3600 + MM * 60 + SS
waktusekarang = CH * 3600 + CM * 60 + CS
#perbedaan waktu
selisih = waktustreaming - waktusekarang
if selisih < 0:
    print("see you on the next pear event!")
else:
    #sisa jam, menit, detik
    jam = selisih // 3600
    selisih %= 3600
    menit = selisih // 60
    detik = selisih % 60
    print(f"{jam:02}:{menit:02}:{detik:02}")