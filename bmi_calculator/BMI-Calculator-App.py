# BMI Calculator
name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print(f"{name}, your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("You're underweight.")
elif 18.5 <= bmi < 25:
    print("You're healthy.")
elif 25 <= bmi < 30:
    print("You're overweight.")
else:
    print("You're obese.")
