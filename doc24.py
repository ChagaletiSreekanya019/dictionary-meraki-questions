# Q24.
# Write a Python program to combine values in python list of dictionaries.
# Sample data: [{"item":"item1","amount": 400}, {"item":"item2","amount":300}, {"item":"item1",
#"amout":750}]
# Expected Output: Counter({item1: 1150, item2: 300}
my_dict = [
{'item': 'item1', 'amount': 400},
{'item': 'item2', 'amount': 300},
{'item': 'item1', 'amount': 750}
]

d = {}
for i in my_dict :
    if i['item'] not in d :
        d.update({i['item'] : i['amount']})
    else :
        d[i['item']] = d[i['item']] + i['amount']
print(d)
    
