
      
import json
import os
accounts={}
user_choice=input("if you want sign up,enter 1,if you want login,press2")
if user_choice=="1":
    uname=input("enter the username to add")
    pwd=input("enter the password to add")
    # create={"account":[uname,pwd]}
    phone=input("enter your phone num")
    email=input("enter the email address")



    accounts.update({"name":uname})
    accounts.update({"password":pwd})
    accounts.update({"phone num":phone})
    accounts.update({"gmail":email})
    accounts=json.dumps(accounts)
    
    with open("accounts.json","w") as f:
        f.write(accounts)
        # json.dump(accounts,f,indent=4)
        # f.write(",\n")
    with open("accounts.json","r") as f:
        accounts=json.load(f)

elif user_choice=="2":
    pass
else:
    print("you must enter 1 or 2")




import json
d={}
d1={}
a=input("enter the signup or login :") 
if a=="signup":
    x=input("enter the user name:")
    y=input("enter the password :")
    z=input("enter the conform pass word:")
    if y>"a" or y<"z" and y>"A" or y<"Z" and y.isdigit():
        if len(y)>=6:
            if y==z:
                print(True)
                d1["username"]=x
                d1["pass word"]=y
                d1["conform pass word"]=z
                D=input("enter the description:")
                F=input("enter the DoB :")
                G=input("enter the gender :")
                d["description"]=D
                d["DoB"]=F
                d["Gender"]=G
                d1["profile"]=d
                with open("signup","w")as f:
                    json.dump(d1,f,indent=4)
            else:
                print("both pass words are not same")
        else:
            print("pass word must be six ") 
    else:
        print("no") 
else:
    username=input("enter the username:")
    password=input("enter the password:")
    d["username"]=username
    d["password"]=password
    print("your logged in successfully")



# import requests
# import json
# res=requests.get("http://saral.navgurukul.org/api/courses")
# a=json.loads(res.text)
# with open("courses.json","w")as f:
#     json.dump(a,f,indent=4)
# with open("courses.json","r")as  f1:
#     d=json.load(f1)
# i=0
# while i<len(a["availableCourses"]):
#     print(i+1,a["availableCourses"][i]["name"],a["availableCourses"][i]["id"])
#     i=i+1
# courses_name=int(input("enter the input1"))
# print(courses_name,a["availableCourses"][courses_name-1]["name"])
# course_id=a["availableCourses"][courses_name-1]["id"]

# res1="http://saral.navgurukul.org/api/courses/" + str (course_id)+"/exercises"
# b=requests.get(res1)
# a1=json.loads(b.text)
# with open("parents.json","w")as f1:
#     json.dump(a1,f1,indent=5)
# # print([courses_name-1]["name"],"-",a[courses_name-1]["id"])
# serial=1
# serial1=1
# list=[]
# list1=[]
# for i in a1["availableCourse"]["exercises"]:
#     if i["parent_exercise_id"]==None:
#         print(serial,i["name"])
#         print(" ",serial1,i["slug"])
#         serial+=1
#         list.append(i)
#         list1.append(i)
#     elif i["parent_exercise_id"]==i["id"]:
#         print(serial,i["name"])
#         serial+=1
#         list.append(i)
#         new=1
#     elif i["parent_exercise_id"]!=i["id"]:
#         print(" ",new,i["name"])
#         new+=1
#         list1.append(i)
# t=open("l.json","w")
# json.dump(list,t,indent=3)
# t=open("l1.json","w")
# json.dump(list1,t,indent=3)

# parent_id=int(input("enter enter no: "))
# serial=1
# idd=list[parent_id-1]["id"]
# for i in list1:
#     if i["parent_exercise_id"]==i["id"]:
#         print(serial,list1[parent_id-1]["name"])
#         serial+=1
#         break
#     else:
#         if i["parent_exercise_id"]!=i["id"]:
#             print(serial,list1[parent_id-1]["name"])
#             print("",list1[parent_id-1]["content"])
#             serial+=1
#             break














# # a=input("if you want to continue ")

# # import requests
# # import json
# # # import o
# # # file=os.path.exists("courses.json")
# # # if file==False:
# # a=requests.get("http://saral.navgurukul.org/api/courses")
# # get_url=a.json()
# # my_file=open("courses.json","w")
# # b=json.dump(get_url,my_file,indent=6)


# # serial=0
# # for i in range(len(get_url)):
# #     serial+=1
# #     for k,v in i.items():
# #         if k=="name":
# #             print(serial,v,"-",get_url[i]["id"])
# # choose=int(input("which course do you  want plese enter:"))
# # idd=get_url[choose-1]["id"]
# # url="http://saral.navgurukul.org/api/courses/"+str(idd)+"/exercises"
# # get_data=requests.get(url)
# # data=get_data.json
