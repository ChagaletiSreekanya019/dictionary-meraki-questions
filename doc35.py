# Q35. Write a Python program to count the number of items in a dictionary value that is a list.
dict = {"Alex": ["subj1","subj2", "subj3"], "David": ["subj1", "subj2"]}
# Sample output: 5
c=0
for i in dict:
    for j in dict[i]:
        c=c+1
print(c)