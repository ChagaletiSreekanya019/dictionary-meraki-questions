# Write a Python program to create a key-value list pairings in a given dictionary.
# Original dictionary:
# d={1:["Jean Castro"],2:["Lula Powell"], 3:["Brian Howell"], 4:["Lynne Foster"],5:["Zachary Simon"]}
# l=[]
# d1={}
# for i,j in d.items():
#         d1.update({i:j[0]})
# l.append(d1)
# print(l)


# for i in range(len(d)):
#     d.update({b[i]:c[i]})
# print(d)


# a="brontosaurus"
# c=list(a)
# print(c)
# d=sorted(c)
# print(d)

# f={}
# for i in d:
#         c=0
#         for j in d:
#                 if i==j:
#                         c=c+1
#         f.update({i:c})
# print(f)


# a="abcadefy"
# d={}
# for i in a:
#         c=0
#         for j in a:
#                 if i==j:
#                         c=c+1
#         d.update({i:c})
# print(d)
# max=0
# for i in d:
#         if d[i]>max:
#                 max=d[i]
# print(max)

d={"w":50,"x":100,"y":"green","z":400}
d1={"x":300,"y":"red","z":600}
d2={}
for i in d:
    for j in d1:
        if i in d1:
            d2[i]=[d[i],d1[i]]
        if j not in d:
            d2[i]=d1[i]
        if i not in d1:
            d2[i]=[d[i]]
print(d2)





