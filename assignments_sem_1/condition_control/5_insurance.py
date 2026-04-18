"""
An Insurance company follows following rules to calculate premium.
● If a person's health is excellent and the person is between 25 and 35 years of age and lives in a
city and is a male then the premium is Rs. 4 per thousand and his policy amount cannot exceed
Rs. 2 lakhs.
● If a person satisfies all the above conditions except that the sex is female then the premium is
Rs. 3 per thousand and her policy amount cannot exceed Rs. 1 lakh.
● If a person's health is poor and the person is between 25 and 35 years of age and lives in a village
and is a male then the premium is Rs. 6 per thousand and his policy cannot exceed Rs. 10,000.
● In all other cases the person is not insured.
Write a program to output whether the person should be insured or not, his/her premium rate and
maximum amount for which he/she can be insured
"""
health=int(input("Is the person healthy(1) or not healthy(0)?  "))
age=int(input("Enter age of person: "))
gender=int(input("Is the person male(1) or female(0)?  "))
location=int(input("Does person lives in city(1) or village(0)? "))

if age>=25 and age<=35 :
    if location == 1 and health == 1 :
        print("Person can be insured")
        if gender==1:
            print("Premium rate: Rs. 4 per thousand")
            print("Policy amount cannot exceed Rs. 2 Lakhs ")
        else:
            print("Premium rate: Rs. 3 per thousand")
            print("Policy amount cannot exceed Rs. 1 Lakh ")
    elif location == 0 and health == 0 and gender == 1:
        print("Person can be insured")
        print("Premium rate: Rs. 6 per thousand")
        print("Policy amount cannot exceed Rs. 10,000 ")
    else:
        print("Person cannot be insured")
else:
    print("Person cannot be insured")