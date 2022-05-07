# d1={1:20,4:56,5:67,7:87,9:65}
# for i in d1:
#     if d1[i]%2==0 or d1[i]%3==0 or d1[i]%5==0 or d1[i]%7==0:
#         print(d1[i],"not")
#     else:
#         print(d1[i],"prime")

# a=["a","b","c","d","e"]
# b=["f","g","h","i","j"]
# i=0
# l=len(b)
# c={}
# while i<len(a):
#     d=({a[i]+b[l-1]})
#     c.update(d)
#     l=l-1
#     i=i+1
# print(c)

# write the python program to drop empty item s from a given dictionary
d1={"c1":"red","c2":"green","c3":None}
# d={}
# for i,j in d1.items():
#     if j is not None:
#         d.update({i:j})
# print(d)

for keys,values in d1:
    if values is None:
        del d1[None]
print(d1)





