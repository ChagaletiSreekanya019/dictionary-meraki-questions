# Q39.Write a Python program to filter a dictionary based on values.
# Original Dictionary:
d={"Cierra Vega": 175, "Alden Cantrell": 180,"Kierra Gentry": 165, "Pierre Cox": 190}
# Marks greater than 170:
# {&#39;Cierra Vega&#39;: 175, &#39;Alden Cantrell&#39;: 180, &#39;Pierre Cox&#39;: 190}
s={}
for i in d:
    if d[i]>170:
        s.update({i:d[i]})
print(s)