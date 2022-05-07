# Q23.Write a Python program to find the highest 3 values of corresponding keys in a
# dictionary.

d1={1:20,4:56,5:67,7:87,9:65}
max=0
for i in d1:
    if d1[i]>max:
        max=d1[i]
print(max)
max1=0
for i in d1:
    if d1[i]>max1:
        if d1[i]!=max:
            max1=d1[i]
print(max1)
max2=0
for i in d1:
    if d1[i]>max2:
        if d1[i]!=max and d1[i]!=max1:
            max2=d1[i]
print(max2)