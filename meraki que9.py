from re import S


l="MISSIIPPI"
s={}
i=0
while i<len(l):
    j=0
    c=0
    while j<len(l):
        if l[i]==l[j]:
            c=c+1
        j=j+1
    s[l[i]]=c
    i=i+1
print(dict(s))
