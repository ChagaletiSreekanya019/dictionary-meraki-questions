# [“neelam”,”programer”,”24”,”2400”,]
# [“komal”,”trainer”,”24”,”20000”]
# [“anuradha”,”HR”,”25”,”40000”]
# [“Abhishek”,”manager”,”29”,”63000”]
import json

emploes={"emp1":{
    "name":"nelam",
    "decignation":"programmer",
    "age":24,
    "salary":24000
    },
    "emp2":{
    "name":"komal",
    "decignation":"programmer",
    "age":20,
    "salary":20000
    },
    "emp3":{
    "name":"anuradha",
    "decignation":"hr",
    "age":25,
    "salary":40000
    },
    "emp4":{
    "name":"abishek",
    "decignation":"manager",
    "age":29,
    "salary":63000
    }

}
# list=json.dumps(emploes,indent=3)
# # print(list)

with open("emploes.json","w") as f:
    # f.write("name","nelam","\nname,abishek")
    # f.close()
    json.dump(emploes,f,indent=3)

