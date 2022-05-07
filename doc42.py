# Q42.
# Write a Python program to check all values are same in a dictionary. Go to the editor
# Original Dictionary:
d={"Cierra Vega": 12, "Alden Cantrell": 12,"Kierra Gentry": 12, "Pierre Cox": 12}
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False
for i in d:
    if d[i]==12:
        print({i:"true"},end="")
    else:
        print("false")