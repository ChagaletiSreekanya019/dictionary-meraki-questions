
mydict=[
{"first":"1"}, 
{"second": "2"}, 
{"third": "1"}, 
{"four": "5"}, 
{"five":"5"}, 
{"six":"9"},
{"seven":"7"}
]
j=[]
for i in range(len(mydict)):
    for l in mydict[i]:
        if mydict[i][l] not in j:
            j.append(mydict[i][l])
print(j)