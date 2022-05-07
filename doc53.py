# Write a Python program to convert a given list of lists to a dictionary.
# Original list of lists:
d=[[1, "Jean Castro","V"], [2, "Lula Powell","V"], [3,"Brian Howell","VI"], [4,"Lynne Foster","VI"], [5,"Zachary Simon", "VII"]]
# Convert the said list of lists to a dictionary:
# {1: [&#39;Jean Castro&#39;, &#39;V&#39;], 2: [&#39;Lula Powell&#39;, &#39;V&#39;], 3: [&#39;Brian Howell&#39;, &#39;VI&#39;], 4: [&#39;Lynne Foster&#39;, &#39;VI&#39;], 5:
# # [&#39;Zachary Simon&#39;, &#39;VII&#39;]}
d2={}
for i in d:
    d2.update({i[0]:i[1:]})
print(d2)
# d1={}
# for i in d:
#     for j in i:
#         d1=[{i[j][0]:i[j][1:]}]
# print(d1)
 