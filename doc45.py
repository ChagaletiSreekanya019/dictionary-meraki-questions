# l= [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000',
# 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'},
# {'id': '#808000', 'color': 'Olive'}]
# l2 = []
# for i in l:
#     if (i['id'] != '#FF0000'):
#         l2.append(i)
# print(l2)


a=[{"name":"mango","quantity":10},{"name":"apple","quantity":2}]
d=[]
c={}
for i in a:
    if i["name"] not in d:
        # c.update({i["name"]:i["quantity"]})
        d.append([i["name"],"=",i["quantity"]])
print(d)



