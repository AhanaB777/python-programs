"""
“List-of-Lists Aggregation: Sales Data”
● Problem: Suppose you receive daily sales data for several products over days. The
data is represented as a list of lists: each inner list corresponds to a day and contains sales
numbers (integers) for different products. For example:
    sales = [
    [5, 3, 0, 2], # day 1: product1 sold 5, product2 sold 3, product3 sold 0, product4 sold 2
    [7, 0, 2, 1], # day 2 ...
    [0, 1, 4, 0],
    ...
    ]

Write a program that:
a. Computes total sales per product over all days.
b. Identifies product(s) with maximum total sales and product(s) with minimum total
sales.
c. Prints a summary: for each product — total sales; then which product(s) sold the most
in total, which the least.
Input: A list of lists of non-negative integers; you may also take number of days and number
of products, or infer from data shape.
Output: Summary as described.
"""
sales=[[5,3,0,2],[7,0,2,1],[0,1,4,0]]

sum_total=[0]*4
for i in sales:
    for j in range(0,len(i)):
        sum_total[j]+=i[j]
print(f"Total sales list product wise:{sum_total}")

max_ts=max(sum_total)
min_ts=min(sum_total)

for i in range(0,len(sum_total)):
    print(f"Total sales of Product {i+1}: {sum_total[i]}")
    if max_ts==sum_total[i]:
        print(f"Product with maximum sale: Product {i+1}")
    if min_ts==sum_total[i]:
        print(f"Product with minimum sale: Product {i+1}")