# Q50.Write a Python program to convert a given dictionary into a list of lists.
# Original Dictionary:
# d={1:"red", 2:"green", 3:"black", 4:"white", 5:"black"}

# Convert the said dictionary into a list of lists:
# [[1, &#39;red&#39;], [2, &#39;green&#39;], [3, &#39;black&#39;], [4, &#39;white&#39;], [5, &#39;black&#39;]]
# Original Dictionary:
# {&#39;1&#39;: &#39;Austin Little&#39;, &#39;2&#39;: &#39;Natasha Howard&#39;, &#39;3&#39;: &#39;Alfred Mullins&#39;, &#39;4&#39;: &#39;Jamie Rowe&#39;}
# Convert the said dictionary into a list of lists:
# [[&#39;1&#39;, &#39;Austin Little&#39;], [&#39;2&#39;, &#39;Natasha Howard&#39;], [&#39;3&#39;, &#39;Alfred Mullins&#39;], [&#39;4&#39;, &#39;Jamie Rowe&#39;]]
# c=[]
# for keys,values in d.items():
#     print([[keys,values]],end="")
#     # c.append(keys)
    # c.append(values)
# print([c])


# d= {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# print([[k,v] for k,v in d.items()])

a={"sejai":20,"sreekanya":15,"kavitha":19}
b=[]
c=[]
sum=0
for k,v in a.items():
    b.append(k)
    c.append(v)
    sum=sum+v
print(b)
print(c)
print(sum)

