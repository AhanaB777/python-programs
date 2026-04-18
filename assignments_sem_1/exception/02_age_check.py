class AgeNotEligibleError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise AgeNotEligibleError("Age must be 18 or above.")
    print("Eligible for registration.")
except AgeNotEligibleError as e:
    print("Custom Exception:", e)
finally:
    print("Program Executed Successfully!")