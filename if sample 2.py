berat = float(input("masukkan berat badan (pounds):"))
tinggi = float(input("masukkan tinggi badan (inchi):"))

#rumus perhitungan
BMI = (703*berat)/(tinggi**2)

if BMI<=18.5:
    print("underweight")
elif 18.5<=BMI<=24.9:
    print("normal")
elif 25.0<=BMI<=29.9:
    print("overweight")
elif BMI>30.0:
    print("obese")