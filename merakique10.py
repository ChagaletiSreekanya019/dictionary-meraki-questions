dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
c=0
for i in dict1:
    if isinstance(dict1[i],list):
        c=c+len(dict1[i])
print(c)
#     c=c+1
# print(dict)
# print(c)
    