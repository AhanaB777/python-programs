#Calculating BMI

w=float(input("Enter weight in kg: "))
h=float(input("Enter height in meters: "))

bmi=w/(h*h)

if bmi<15:
    print("Starvation")
elif bmi>=15.1 and bmi<=17.5 :
    print("Anorexic")
elif bmi>=17.6 and bmi<=18.5 :
    print("Underweight")
elif bmi>=18.6 and bmi<=24.9 :
    print("Ideal")
elif bmi>=25 and bmi<=25.9 :
    print("Overweight")
elif bmi>=30 and bmi<=30.9 :
    print("Obese")
else :
    print("Morbidly obese")