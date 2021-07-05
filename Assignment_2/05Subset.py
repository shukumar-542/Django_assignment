# list1 = {1,2,3,4,5,6}
# list2 = {6,7,8,9,10}
#
# if (list1.intersection(list2)):
#     print("true")
# else:print("false")

list1 = []
list2 = []

l1 = int(input("enter the value for list: "))
for i in range(0,l1):
    val1 = int(input("enter the number: "))
    list1.append(val1)
print("first list is: ",list1)


l2 = int(input("enter the value for list : "))
for i in range(0,l2):
    val2 = int(input("enter the number: "))
    list2.append(val2)
print("Second  list is: ",list2)

list1 = set(list1)
list2 = set(list2)

if (list1.intersection(list2)):
    print("true")
else:print("False")