print(sum([12,2]))

l = [1, 2, 3, 4, 5, 6, 7]
for i in range(10):
    print(i)
# generator / custom iteration

def myrange(val):
    for i in range(0 , val):
        yield i

val = myrange(10)
print(next(val))
print(next(val))
print(next(val))

# for i in  myrange(20):
#     print(i)


getnumber = lambda a:a*a
print(getnumber(140))


