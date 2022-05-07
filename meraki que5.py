list1=["one","two","three","four","five"]

list2=[1,2,3,4,5,]
list3={}
for i in range(len(list1)):
        list3.update({list1[i]:list2[i]})
print(list3)