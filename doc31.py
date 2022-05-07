# Q31.. Write a Python program to get the top three items in a shop. Go to
# the editor
d1= {"item1": 40.50, "item2":35,"item3": 41.30, "item9":55, "item7": 24}
# Expected Output:
# item4 55
# item1 45.5
max=1
for i in d1:
    if d1[i]>max:
        max=d1[i]
        key=i
print(key,max)
max1=0
for i in d1:
    if d1[i]>max1:
        if d1[i]!=max:
            max1=d1[i]
print(i,max1)


