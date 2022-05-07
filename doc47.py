# A Python Dictionary contains List as value. Write a Python program to clear the list values in
# the said dictionary.
# Original Dictionary:
# def test(dictionary):
#     for key in dictionary:
#         dictionary[key].clear()
#     return dictionary

d= { 
            'C1' : [10,20,30], 
            'C2' : [20,30,40],
            'C3' : [12,34]
            }
# # print(test(dictionary))
# for key in d:
#     d[key].clear()
# print(d)

for i in d:
    d[i].clear()
print(d)



