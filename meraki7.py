# Text.txt:-  
#  Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 29

import json
emp1={
    "name":"abishek",
    "designation":"ceo of navgurukul",
    "gender":"male",
    "age":"34"
}

x=json.dumps(emp1,indent=3)
print(x)