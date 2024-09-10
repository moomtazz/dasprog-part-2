jumlah_kucing = list(map(int, input().split()))
kucing_lompat= int(input())
jumlah_lompat= int(input())

x, y, z = map(int, input().split())

for i in range(jumlah_lompat):
    jumlah_kucing = jumlah_kucing[-kucing_lompat:] + jumlah_kucing[:-kucing_lompat]

print(jumlah_kucing[x], jumlah_kucing[y], jumlah_kucing[z])