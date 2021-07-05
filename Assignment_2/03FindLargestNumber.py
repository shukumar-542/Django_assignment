a = []
n = int(input("enter the number of element:"))

for i in range(0,n):
    val= int(input("enter the number"))
    a.append(val)
max_num = 0
for i in a:
    if i > max_num:
        max_num = i
print("The largest number in the list",max_num)