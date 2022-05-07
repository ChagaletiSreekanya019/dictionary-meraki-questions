l= [1, 2, 3, 4]
d={}
for i in l:
    d[i]={}
print(d)

l = [1, 2, 3, 4]
d=current = {}
for i in l:
    current[i] = {}
    current = current[i]
print(d)