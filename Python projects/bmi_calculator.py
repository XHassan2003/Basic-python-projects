# BMI Calculator:

weight = float(input("Enter you weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = round(weight / height ** 2)
print(bmi) 