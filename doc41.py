
# .Write a Python program to filter the height and width of students, which are stored in a
# dictiQ41onary.
# Original Dictionary:

d={"Cierra Vega": (6.2, 70), "Alden Cantrell": (5.9, 65),"Kierra Gentry": (6.0, 68), "Pierre Cox": (5.8,
66)}
# Height  6ft and Weight 70kg:
# {&#39;Cierra Vega&#39;: (6.2, 70)}d
for keys,values in d.items():
    if values[0]>=6.0 and values[1]>=70:
        print(keys,values)

#         if k[1]>=6:
#             print(j,k)
#         if k[2]>=70:
#             print(j,k)
        
# def filter_data(students):
#     result = {k: s for k, s in students.items() if s[0] >=6.0 and s[1] >=70}
#     return result    
 

