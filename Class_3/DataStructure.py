# list ,Tuple,Set ,Dictinory
l = [1,2,3,2,2,1.5,"four",1.5]
print(type(l))
print(l)

l.append("ten")
print(l)
l.insert(4,5)
print(l)
print(l.index(3))
print(l.count(2))
print(l.pop(0))
print(l)

list = [1,5,6,4,8,2,4,5,10]

print("before sorting",list)
list.sort()
print("after sorting",list)
list.reverse()
print(list)

for x in l:
    print(type(x))
    print(x)


# Nasted list
l = [[1, 2, [3, 4]], [5, 6, 7], [1.5, 1.6, 2.9]]
print(l)
l2=(l[0][2])
print(l2[1])

#Mutable and immutable

l[0] = 100
print(l)

t = (1,2,3,4,5,6)
print(t)


#set

s = {1,2,3,4,5,5}
print(type(s))
print(s)
s.add(15)
print(s)

s2 ={6,4,7,5,9}
print(s.union(s2))
print(s2.union(s))
print(s.intersection(s2))
print(s.issubset(s2))