""" 
Q2. Bank Compare 
There are two banks - Bank A and Bank B. Their interest rates vary. You have received 
offers from both banks in terms of the annual rate of interest, tenure, and variations of 
the rate of interest over the entire tenure.You have to choose the offer which costs you 
least interest and reject the other. Do the computation and make a wise choice. 
The loan repayment happens at a monthly frequency and Equated Monthly Installment 
(EMI) is calculated using the formula given below : 

EMI = loanAmount * monthlyInterestRate / ( 1 - 1 / (1 + 
monthlyInterestRate)^(numberOfYears * 12))

Constraints: 
1 <= P <= 1000000 
1 <=T <= 50 
1<= N1 <= 30 
1<= N2 <= 30

Input Format: 
• First line: P principal (Loan Amount) 
• Second line: T Total Tenure (in years). 
• Third Line: N1 is the number of slabs of interest rates for a given period 
by Bank A. First slab starts from the first year and the second slab starts 
from the end of the first slab and so on. 
• Next N1 line will contain the interest rate and their period. 
• After N1 lines we will receive N2 viz. the number of slabs offered by the 
second bank. 
• Next N2 lines are the number of slabs of interest rates for a given period 
by Bank B. The first slab starts from the first year and the second slab 
starts from the end of the first slab and so on. 
• The period and rate will be delimited by single white space. 

Output Format: Your decision either Bank A or Bank B. 


"""
# p=float(input("Principle : "))
# t=int(input("Total tenure: "))
# n1=int(input("Number of slabs of Bank A: "))
# rate=period=[]
# for i in range(n1):
#     a=input().split()
#     l=list(map(int,a))
#     print(l)
p=500000
t=26
bank_a=[[13,9.5],[3,6.9],[10,5.6]]
n1=len(bank_a)
bank_b=[[14,8.5],[6,7.4 ],[6,9.6]]
n2=len(bank_b)

emi_a=0
for i in range(0,n1):
    x=0
    y=bank_a[i][x]
    r=bank_a[i][x+1]
    v=p*r/(1-1/(1+r)**(y*12))
    emi_a+=v
print(f"Bank A: {emi_a}")

emi_b=0
for i in range(0,n2):
    x=0
    y=bank_b[i][x]
    r=bank_b[i][x+1]
    v=p*r/(1-1/(1+r)**(y*12))
    emi_b+=v
print(f"Bank B: {emi_b}")

if emi_a>emi_b:
    print("Choose Bank B")
else:
    print("Choose Bank A")
