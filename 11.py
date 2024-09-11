#Input nilai m dan n
m = int(input("masukkan nilai m (dengan m>n):"))
n = int(input("masukkan nilai n (dengan n<m):"))

#Menghitung sisi segitiga
Sisi1 = m**2 - n**2
Sisi2 = 2*m*n
Sisi_miring = m**2 + n**2

#Panjang setiap sisi segitiga
print(f"Triple Phytagoras yang dihasilkan:")
print(f"Sisi A = {Sisi1} ")
print(f"Sisi B = {Sisi2} ")
print(f"Sisi C = {Sisi_miring} ")