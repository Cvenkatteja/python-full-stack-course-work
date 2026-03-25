"""def wish (name):
    return f"hello{name},welcome to hte python"

wish = lambda name:f"{hello} ,welcome to the python"



print(wish("vemkat"))
print(wish("buhvan"))"""

'''def add(a,b,c):
    return (a+b+c)/3

add1 =lambda a,b,c:(a+b+c)/3


print(add(1,2,3))
print(add1(6,7,8))

def iseven(n):
    if n%2==0:
        return"even"
    else:
        return"odd"
iseven1 =lambda n:"even"if n%2==0 else "odd"

print(iseven(19))
print(iseven1(20))

def greater(a,b):
    if a>b:
        return a
    else:
        return b

greater1 = lambda a,b:a if a>b else b

print(greater(19,9))
print(greater1(28,79))

def isvowel(a):
    if a in vol:
        return "vol"
    else:
        return"con"


def fun(l):
    for i in range(len(l)):
        l[i]=l[i].title()
    return l
l=["anju","venkat","bhuvan","kishore"]


res=list(map(lambda i:i.title(),l))#seprate lambda code


print(fun(l))
print(res)
    
#doubt
def fun(l):
    res=[]
    for i in range(len(l)):
        if l[i]%3==0:
            res.append(l[i])
    return res

l= [20,30,40,50,60,80,90,100]

res= list(filter(lambda i:i%3==0,1))



print(fun(l))
print(res)'''

l= {'laptap':True,
    'charger':True,
    'mouse':False,
    'tablet':False
    }
res =list(filter(lambda i:l[i],l))

print(res)




l = [1,2,3,4,4,5,6,7,8,9,0,4,6,9,0,87,6,5,5]

res=list(filter(lambda i:i%2==0,l))

print(res)




from functools import reduce

l=[1,2,3,4,4,5,6,7,8,9,4,6,9,87,6,5,5]

res = reduce (lambda a,b:a*b,l)

print(res)


from functools import reduce

l=['python','java','c++','html']

res = reduce (lambda a,b:a+'  '+b,l)

print(res)


































