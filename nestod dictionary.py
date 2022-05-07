# b={"a":1,{"c":2},"d":3}

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
# # print(people)
# for x,y in people.items():
#     for k,v in y.items():
#         print([k,v],end="")




# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

# (people[1]['name'])=["sai"]
# people[1]["villaga"]=["chennai"]
# # # print(people[1]['age'])
# # # print(people[1]['sex'])
# print(people)


# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

# # # people[3] = {}

# del people[1]['name']
# print(people)
# # people[3]['age'] = '24'
# people[3]['sex'] = 'Female'
# people[3]['married'] = 'No'

# print(people[3])
for x ,y in people.items():
    print(x)
    for key in y:
        print([key+":",y[key]])

# a=["husna","pinki","shaik"]
# b={}
# i=0
# for i in a:
#     c=0
#     for j in i:
#         c=c+1
#     b.update({i:c})
# print(b)
# while i<len(a):
#     c=0
#     j=0
#     while j<len(a[i]):
#         c=c+1
#         b.update({a[i]:c})
#         j=j+1
#     i=i+1
# print(b)

# d1=[{"first":"1"},{"second":"2"},{"four":"5"},{"five":"5"}]
# d2=[]
# for i in d1:
#     for k,v in i.items():
#         if v not in d2:
#             d2.append(v)
# print(d2)

# dict = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32'}
# dict1=(sorted(dict.items()))
# print(dict1)
# dict2=(sorted(dict.values()))
# print(dict2)

# a=["red","blue","orange"]
# d=dict.fromkeys(a,"colour")
# print(d)



# a=[[1,2][3,4][5,[6,7]]]
# d={}
# for i in a:
#     d.update({i[0]:i[1]})
# print(d)

# # out put{1:2,3:4,5:[6,7]


# a=["a","b","c","d"]
# d=dict(enumerate(a))
# print(d)


# d={"red":1,"green":2,"white":3}
# d1=[]
# for i,j in d.items():
#     d1.append([i,j]) 
# print(d1)

# d={"sree":34,"hani":20,"swapna":67,"pandu":20}
# b=20
# d1=[]
# for i,j in d.items():
#     if j==b:
#         d1.append(i)
# print(d1)


d=[{"name":"sreekanya","age":24},{"name":"swapna","age":5},{"name":"pandu","age":2}]
d1=[]
for i in d:
    s=i.get("age")
    j=i.get("name")
    d1.append([s,j])
print(d1)

# d={1:("amit",25000),2:("suman",30000),3:("ravi",36000)}
# d1=list(d.values())
# for i in d1:
#     if i[1]>25000:
#         print(i[0])



# d={1:"greek",2:{3:{4:{}}}}
# c=0
# j="{"
# for i in len(d):
#     if i==j:
#         c=c+1
# print(c)