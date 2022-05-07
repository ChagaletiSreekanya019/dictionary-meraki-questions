d = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]

sum=0
for i in d:
    if i["id"] in d:
        sum=sum+d[i]
print(sum)

# n={"n1"}
# s={i:sorted(j) for i,j in n.items}
# print(s)