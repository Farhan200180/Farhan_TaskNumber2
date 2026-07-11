weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in meters: "))

if weight<=0 or height<=0:
    print("Weight and height must be positive values.")
else:
    BMI=weight/(height**2)
    if BMI<18.5:
        print(f"Your BMI is {BMI:.2f}. You are underweight.")
    elif BMI<25:
        print(f"Your BMI is {BMI:.2f}. You have a normal weight.")
    elif BMI<30:
        print(f"Your BMI is {BMI:.2f}. You are overweight.")
    else:
        print(f"Your BMI is {BMI:.2f}. You are obese.")