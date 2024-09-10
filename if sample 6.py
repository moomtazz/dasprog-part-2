x = float(input("masukkan koordinat x:"))
y = float(input("masukkan koordinat y:"))

if x==0 and y==0:
    print("titik berada di koordinat pusat")
elif x==0:
    print("titik berada di sumbu x")
elif y==0:
    print("titik berada di sumbu y")
elif x>0 and y>0:
    print("titik berada di kuadran I")
elif x<0 and y>0:
    print("titik berada di kuadran II")
elif x<0 and y<0:
    print("titik berada di kuadran I")
elif x>0 and y<0:
    print("titik berada di kuadran IV")