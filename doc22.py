l={"1":["a","b"],"2":["c","d"]}
# for x,y in l.values():
#     for i in l["1"]:
#         for j in l["2"]:
#             print(i,j)
# for i in l:
for x,y in l.values():
    for j in y:
        print(j,y)