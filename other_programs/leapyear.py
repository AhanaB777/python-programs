#PROGRAM TO CHECK LEAP YEAR
#take input
year=int(input("Enter year to check leap year: "))

#using conditional operator
if year%400==0 or year%100!=0 and year%4==0 :
    print(f"The year {year} is a leap year")
else :
    print(f"The year {year} is not a leap year")

#USING CONDITIONAL OPERATORS

status="a leap Year" if year%400==0 or year%100!=0 and year%4==0 else "not a leap year"
print(f"The year {year} is {status}")