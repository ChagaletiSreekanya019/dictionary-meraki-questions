

# import json

# name={
#   "data": [
#     {
#       "color": "red",
#       "value": "#f00"
#     },
#     {
#       "color": "green",
#       "value": "#0f0"
#     },
#     {
#       "color": "blue",
#       "value": "#00f"
#     },
#     {
#       "color": "black",
#       "value": "#000"
#     }
#   ]
# }

# # colors=json.dumps(name,indent=4)
# with open("sample json2","w") as f:
#     json.dump(name,f,indent=4)
  

# with open('sample json2', 'r') as openfile:
  
#     # Reading from json file
#     json_object = json.load(openfile)
  
# print(json_object)
# print(type(json_object))


# import json
# dictionary ={
#     "name" : "sathiyajith",
#     "rollno" : 56,
#     "cgpa" : 8.6,
#     "phonenumber" : "9976770500"
# }
  
# with open("sample.json", "w") as outfile:
#     json.dump(dictionary,outfile,indent=3)
# with open("sample.json","r") as outfile:
#    js=json.load(outfile)
# print(js)
# import json
# name={
#     "data":{
#         "color":"black",
#         "fruit":"banana"
#     }
# }
# with open("sree","w")as f:
#     json.dump(name,f,indent=4)




l=["red","orange","black"]
k=[1,2,3]
d={}
i=0
# # for i in range(len(k)):
# #     d.update({k[i]:l[i]})
# # print(d)
while i<len(l):
    j=0
    while j<len(k):
        d.update({l[i]:k[i]})
        j=j+1
    i=i+1
print(d)