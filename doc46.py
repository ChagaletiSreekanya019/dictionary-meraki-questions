l=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50','r': '60'}]
d=[]
for i in l:
    for a,b in i.items():
        f=({a:int(b)})
        d.append(f)
print(d)
