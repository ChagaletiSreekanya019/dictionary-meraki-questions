# num=int(input("enter the num"))
# dic={}
# for i in range(1,15+1):
#     dic.update({i:i*i})
# print(dic,end="")

n=int(input("enter the number"))
dic={}
for i in range(1,n+1):
    dic[i]=i ** 2
print(dic)