# write the python program to map two lists into a dictionary

l=["red","orange","black"]
k=[1,2,3]
d={}
for i in range(len(l)):
    d.update({l[i]:k[i]})
print(d)


a=["a","b","c"]
d={}
for i in range(len(a)):
    d.update({a[i]:54})
print(d)
