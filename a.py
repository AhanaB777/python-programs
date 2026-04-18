
m1={'pl1': 20, 'pl2':30, 'pl3' : 50}
m2={'pl3':10, 'pl5': 50 , 'pl1' : 30}
total={}
for d in (m1, m2):
    for k,v in d.items():
        if k in total:
            total[k]+=v
        else:
            total[k]=v
print
