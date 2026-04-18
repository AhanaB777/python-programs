""" Program to find the player who scored maximum over two separate matches """

m1={'pl1': 20, 'pl2':30, 'pl3' : 50}
m2={'pl3':10, 'pl5': 50 , 'pl1' : 30}
total={}

for pl in m1.keys():
    total[pl] = m1[pl]

for pl in m2.keys():
    if pl in total:
        total[pl] += m2[pl]
    else:
        total[pl] = m2[pl]

max=0
for pl in total.keys():
    if total[pl] > max :
        max=total[pl]
        player=pl

print("Player : ", player , " max score : ",total[player])
