# Q52. Write a Python program to find the specified number of maximum values in a given
# dictionary.
# Original Dictionary:
d={"a": 5,"b":14, "c": 32, "d": 35, "e": 24,"f": 100,"g": 57, "h": 8, "i": 100}
# 1 maximum value(s) in the said dictionary:
# [&#39;f&#39;]
max=0
for i in d:
    if d[i]>max:
        max=d[i]
        key=i
print(key)
