color = input("masukkan warna tabung:").upper()

#menentukan isi berdasarkan huruf warna
if color[0] == 'O':
    contents = "ammonia"
elif color[0] == 'B':
    contents = "carbon monoxide"
elif color[0] == 'Y':
    contents = "hydrogen"
elif color[0] == 'G':
    contents = "oxygen"
else:
    contents = "unknown"

# hasil
print(f"isi dari tabung adalah: {contents}")