l=[30,78,90,54,34,30,78]
r=[]
print(l)
for i in l:
    if i not in r:
        r.append(i)
l=r
print(l)
