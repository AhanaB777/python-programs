""" Problem Statement : Round Grades to the nearest multiple of 5 if difference between grades and the next multiple 
        of 5 is less than 3. For grades below 38 no rounding required as it will be a fail.

        eg: grade 74; next multiple of 5 => 75; difference 75-74 = 1; round 74 to 75 

 """

grades=[38,46,67,74]
n=len(grades) 
res=[]
for i in range(0,n) :
    if grades[i] < 38 :
        res.append(grades[i])
    else:
        if grades[i]%5 >= 3:
            q=grades[i]//5
            res.append((q+1)*5)
        else:
            res.append(grades[i])
print(res)