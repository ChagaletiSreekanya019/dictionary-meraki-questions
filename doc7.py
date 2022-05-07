# sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
d4={}
for i in d1:
    # for i in d2:
        # for i in d3:
    d4.update(d1)
    d4.update(d2)
    d4.update(d3)
print(d4)
