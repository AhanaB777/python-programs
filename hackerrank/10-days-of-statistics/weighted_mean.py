" Goal : Find weighted mean of two arrays X and W "

x=[4,7,9]
w=[2,5,1]
prod=[a*b for a,b in zip(x,w)]
print(prod)
prod_sum=sum(prod)
print(prod_sum)
w_sum=sum(w)
print(w_sum)
weighted_mean=prod_sum/w_sum
print(round(weighted_mean,1))