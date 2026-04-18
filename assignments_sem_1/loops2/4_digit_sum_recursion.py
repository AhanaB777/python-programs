"""
Digit-Sum Recursion with Loop”
● Problem statement: Write a program that repeatedly asks the user for a positive integer.
For each integer, compute the “digit sum” (sum of its digits). If that digit sum is greater
than 9, take that result and again compute its digit sum, continue until the result is a single digit (≤ 9). 
Print the number of iterations it took and the final single-digit result.
Repeat this entire process for each integer entered until the user enters zero or a
negative number to stop. At the end, print how many integers were processed.
● Input: A sequence of integers. Terminate when input ≤ 0.
● Output: For each integer: print “Iterations: X, Final digit: Y”. After termination: print “Total
numbers processed: N”.

"""
count=0
while True :
    num = int(input("Enter a positive integer (Enter 0 or negative to stop): "))
    if num<=0 : 
        print(f"Total numbers processed:{count}")
        break

    count+=1
    iteration=0

    while num>9 :
        digit_sum = 0
        temp = num

        while temp!= 0 :
            rem = temp%10
            digit_sum += rem
            temp//=10
        
        num=digit_sum
        iteration+=1

    print(f"Iterations: {iteration}, Final digit: {num}")


    

