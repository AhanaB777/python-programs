"""Q9 
Coins Distribution Question (or Coins Required Question) 
Problem Description  
Find the minimum number of coins required to form any value between 1 to N, both inclusive. 
Cumulative value of coins should not exceed N. Coin denominations are 1 Rupee, 2 Rupee and 5 
Rupee. 
Let's understand the problem using the following example. Consider the value of N is 13, then 
the minimum number of coins required to formulate any value between 1 and 13, is 6. One 5 
Rupee, three 2 Rupee and two 1 Rupee coins are required to realize any value between 1 and 13. 
Hence this is the answer. 
However, if one takes two 5 Rupee coins, one 2 rupee coins and two 1 rupee coins, then to all 
values between 1 and 13 are achieved. But since the cumulative value of all coins equals 14, i.e., 
exceeds 13, this is not the answer.  
Input Format  
A single integer value 
Output Format  
Four Space separated Integer Values  
1st - Total Number of coins  
2nd - number of 5 Rupee coins.  
3rd - number of 2 Rupee coins.  
4th - number of 1 Rupee coins.  
Constraints  
0<n<1000 """
# n=13
# o=1
# t=2
# f=5
# l=[0,0,0,0]
# for i in range(n):
    