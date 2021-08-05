# def add(*args ,**kwargs):
#     return kwargs
# print(add (a=10 , b= 20))



def getsome(a):
    return a

def setsome(a):
    b = getsome(a)
    print(b)


setsome(10)