
# Q40. Write a Python program to convert more than one list to nested dictionary.
# Original strings:
a=["S001", "S002", "S003", "S004"]
b=["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"]
c=[85, 98, 89, 92]
# Nested dictionary:
# [{S001: {Adina Park:85}}, {S002: {Leyton Marsh: 98}}, {S003: {Duncan Boyle: 89}},
# {&#39;S004&#39;: {&#39;Saim Richards&#39;: 92}}]
# d1={}
# # for i in a:


e=[]
for i in range(len(a)):
        d={}
        d.update({a[i]:{b[i]:c[i]}})
        e.append(d)
print(e)

