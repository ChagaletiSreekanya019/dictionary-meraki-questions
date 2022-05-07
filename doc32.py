# Q32.Write a Python program to get the key, value and item in a dictionary.
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# Sample Output:
# key value count
# 1 10 1
# 2 20 2
# 3 30 3
# 4 40 4
# 5 50 5
# 6 60 6

# c=0
# for i in dict_num:
#     print(i," ",dict_num[i]," ",i)
# c=0
# for i in dict_num:
#     c=c+1
#     print(i,"",dict_num[i],"",c)


# d1=[{},{},{}]
# def fun(d1):
#     for i in d1:
#         if i=={}:
#             return True
#         else:
#             return False
# d1=[{1,2},{},{}]
# print(fun(d1))


d={1:"red",2:"green",3:"black",4:"white" ,5:"black"}
l=[]
for i,j in d.items():
    # for j in d:
        l.append([i,j])
print(l)