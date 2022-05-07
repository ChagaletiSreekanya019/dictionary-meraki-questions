# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

a="w3resource"
l={}
i=0
while i<len(a):
    j=0
    c=0
    while j<len(a):
        if a[i]==a[j]:
            c=c+1
        j=j+1
    l.update({a[i]:c})
    i=i+1
print(l)

a="sreekanya"
l={}
i=0
while i<len(a):
    j=0
    c=0
    while j<len(a):
        if a[i]==a[j]:
            c=c+1
        j=j+1
    l[a[i]]=c
    i=i+1
print(l)
