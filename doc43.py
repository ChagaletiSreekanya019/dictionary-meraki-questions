
l = {('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)}
d = {}
# for i in l:
#     if i[0] not in d.keys():
#         d.update({i[0]:[i[1]]})
#     elif i[0] in d.keys():
#         d[i[0]].append(i[1])
# print(d)
for i in l:
    if i[0] not in d.keys():
        d.update({i[0]:[i[1]]})
    elif i[0] in d.keys():
        d[i[0]].append(i[1])
print(d)



