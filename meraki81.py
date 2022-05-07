a=["neelam","programer","24","24000"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
f={}
g={}
h={}
k={}
s={}
for i in range(len(a)):
    f.update({"name":a[0],"decignation":a[1],"age":a[2],"salary":a[3]})
s.update({"emi1":f})
for i in range(len(b)):
    g.update({"name":b[0],"decignation":b[1],"age":b[2],"salary":b[3]})
s.update({"emi2":g})
for i in range(len(c)):
    h.update(({"name":c[0],"decignation":c[1],"age":c[2],"salary":c[3]}))
s.update({"Emi3":h})
for i in range(len(d)):
    k.update({"name":a[0],"decignation":a[1],"age":a[2],"salary":a[3]})
s.update({"emi4":k})
# print(s)

import json
# emplies=json.dumps(s,indent=4)
# print(emplies)

with open("sreekanya","w") as f:
    json.dump(s,f,indent=4)

with open("sreekanya","r")as f:
    e=json.load(f)
print(e)