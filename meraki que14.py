
# {'bijender':45,'deepak':60,'param':20,';'anjili':30,'roshini':50}

# Visualize
# Expected result in Ascending Order:

# {'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}
# Expected result in Descending Order:

# {'deepak':60,'roshini':50,'bijender':45,'anjili':30,'param':20}

a={'bijender':45,'deepak':60,'param':20,"anjili":30,'roshini':50}
# d={}
# for i in sorted(a.values()):
#     print({i:a[i]},end="")
#     # d.update(a)
# # print(dict(d))
c={}   
for i in a:
    # c=a.sorted("keys")
    d=sorted(a.values())
    c.update({i:d[i]})
# print("c:d")
print(c)