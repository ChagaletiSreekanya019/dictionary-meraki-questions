# write a python program to get the maximum and minimum volue in a dictionary

d={1:24,2:48,3:56,4:48}
k=list(d.values())
max=0
i=0
while i<len(k):
    if k[i]>max:
        max=k[i]
    i=i+1
print(max)
min=k[0]
while i<len(k):
    if min>k[i]:
        min=k[i]
    i=i+1
print(min)



# def length(str):
#     d=list(str.split(" "))
#     return len(d[-1])
# str="name not there in"
# print(length(str))


# s="my name is khushbu"
# i=1
# c=0
# while i<len(s):
#     if s[-i]==" ":
#         break
#     c=c+1
#     i=i+1
# print(c)





# def length(str):
#     lis = list(str.split(" "))
#     return len(lis[-1])
# str = "my name is sreekanya"
# print(length(str))
 
