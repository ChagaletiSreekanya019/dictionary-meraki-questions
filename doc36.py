# Q36.Write a Python program to match key values in two dictionaries.
d1= {"key1": 1, "key2": 3, "key3": 2}
d2= {"key1": 1, "key2": 2}
# Expected output: key1: 1 is present in both x and y
d3={}
for i in d1:
    for j in d2:
        # a=d1[i]
        # b=d2[j]
        # if i==j and a==b:
        #     print(i,":",a,"is present in both d1 and d2")
        if i==j and d1[i]==d2[j]:
            print(i,":",d1[i],"is present in both d1 and d2")