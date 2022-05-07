# Write a Python program to print a dictionary in table format.
my_dict = {"C1":[1,2,3],"C2":[5,6,7],"C3":[9,10,11]}
# Sample Output:
# C1 C2 C3
# 1 5 9
# 2 6 10
# 3 7 11

# for i in my_dict:
#     print(i,end=" ")
a=[]
for i in my_dict:
    b=my_dict[i]
    a.append(b)
print(a)
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        sum=a[i][j]
        print(sum,end=" ")
        j=j+1
    print()
    i=i+1
    


