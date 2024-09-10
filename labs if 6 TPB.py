def apakah_prima(n):
    if n<2:
        return False
    for i in range (2,n):
        if n%i==0:
            return False
    return True

n = int(input("masukkan angka:"))

if apakah_prima(n):
        print("it's a prime")
else:
     print("it's not a prime")