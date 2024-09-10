depan, belakang, waktu = map(int, input().split())
merah, kuning, hijau = 20, 5, 60

satu_siklus = merah + kuning + hijau
jumlah_mobil = depan + belakang + 1

jumlah_siklus = waktu//satu_siklus
sisa_waktu = waktu%satu_siklus

if sisa_waktu > 25:
    sisa_hijau = sisa_waktu - 25
else:
    sisa_hijau = 0

total_hijau = hijau + jumlah_siklus + sisa_hijau
mobil_lewat = total_hijau//5

if jumlah_mobil <= mobil_lewat:
    print("YES!",0)
else:
    print("NO!", jumlah_mobil-mobil_lewat)