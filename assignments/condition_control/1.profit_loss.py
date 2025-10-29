"""
    If cost price and selling price of an item is input through the keyboard, write a program to
    determine whether the seller has made profit or incurred loss. Also determine how much profit he
    made or loss he incurred
"""
cp=float(input("Enter Cost Price of item: "))
sp=float(input("Enter Selling Price of item: "))

if sp>cp:
    profit=sp-cp
    print(f"The seller made profit of Rs. {profit}")
elif cp>sp:
    loss=cp-sp
    print(f"The seller incurred loss of Rs. {loss}")
else:
    print("There is no loss and no profit")