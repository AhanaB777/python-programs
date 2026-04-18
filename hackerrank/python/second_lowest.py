""" Display name of second lowest marks in alphabetical order if more than one """

s = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

scores = sorted({score for _, score in s})
# print(scores)

m=scores[1]
# print(m)

result = sorted(name for name,score in s if score==m)

for n in result:
    print(n)
