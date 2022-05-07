# write the pythin program to remove a key a dictionary

# from locale import DAY_1

# d1={"a":2,"b":2,"c":3}
# multi=1
# for i in d1:
#     multi=multi*d1[i]
# print(multi)

d1={"a":2,"b":2,"c":3,"d":8,"e":8,"g":9}
for i in d1:
    if d1[i]%2==0:
        print({d1[i],"even"},end="")
    else:
        print({d1[i],"odd"},end="")
