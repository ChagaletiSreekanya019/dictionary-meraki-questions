a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# print({value:len(value) for key, value in a.items()})
for key,value in a.items():
    print([len(value),value],end="")
