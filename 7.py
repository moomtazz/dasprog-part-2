#Program untuk menghitung BTU yang didistribusikan ke rumah 

#Jumlah BTU pada setiap barel
BTU_Per_Barrel = 5800000
#Jumlah galon pada setiap barrel
Galon_Per_Barrel = 42

#Input jumlah galon minyak yang dibakar
Jumlah_Galon_Minyak= int(input(" masukkan jumlah galon minyak yang dibakar: "))
#Input efisiensi
Efisiensi= 0.65 

#Hitung jumlah BTU pada setiap galon
BTU_Per_Galon = BTU_Per_Barrel/Galon_Per_Barrel
#Hitung total BTU
Total_BTU = Jumlah_Galon_Minyak*BTU_Per_Galon
#Jumlah BTU pada setiap rumah
BTU_Rumah = Total_BTU*Efisiensi

print("Jumlah BTU pada setiap rumah:", {BTU_Rumah})