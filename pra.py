a={1:2,3:4,5:6,6:7,6:7,9:9,7:9}
# d={}

# for k,v in a.items():
#     if v not in d:
#         d.update({k:v})
#     else:
#         d.update({k:v})
# print(d)
d={}
for k,v in a.items():
    if v%2==0:
        d.update({k:"even num"})
    elif v%2!=0:
        d.update({k:"odd num"})
print(d)
