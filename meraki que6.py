# dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
# print(dic)

dict={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
dic={}
for i in dict:
    if i not in dic:
        dic.update(dict)
print(dic)

# n=int(input("enter the num"))
# i=0
# sum=0
# while i<n:
#     a=int(input("enter any number"))
#     sum=sum+a
#     i=i+1
# print(sum)


