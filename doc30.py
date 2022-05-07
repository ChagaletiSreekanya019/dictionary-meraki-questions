student_list = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}

# for key,values in list(student_list.items()):
#     word = " "
#     for i in key:
#         if i != " ":
#             word += i
#         print(word)
# student_list[word] = student_list.pop(key)

# print(student_list)

d={}
for i in student_list:
    c=""
    j=0
    while j<len(i):
        if i[j]!=" ":
            c=c+i[j]
        j=j+1
    d.update({c:student_list[i]})
print(d)