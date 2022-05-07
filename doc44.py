# Q44.Write a Python program to split a given dictionary of lists into list of dictionaries.
# Original dictionary of lists:
d={"Science": [88, 89, 62, 95], "Language": [77, 78, 84, 80]}
# Split said dictionary of lists into list of dictionaries:
d= {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
#output
# [{'Science':88},{'Science':89},{'Science':62},{'Science':95},{'Language':77},{'Language':78},{'Language':84}..]

# res=[]
# # a,b=d.values()

# for i in range(len(d)):
#     for j,k in i:
#         b=({j:k[i]})
#         res.append(b)
# print(res)
d1={}
c=[]
for i,j in d.items():
    for k in j:
        d1.update({i:k})
        c.append(d1)
print(c)

