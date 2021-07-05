list =[1,2,3,4,5,2,6,5,1]
result = []

for i in list:
    if i not in result:
        result.append(i)

print(result)