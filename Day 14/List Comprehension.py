'''a=[]
for i in range(1,100):
    if i%2==0:
        a.append(i)
print(a)'''
l=[i for i in range(1,100) if i%2==0]
print(l)

l=[i for i  in range(3,100,3) if i*3]
print(l)

s='python programming'
vol='aeiouAEIOU'
l=['*'if i in vol else i for i in s]#why we are wiriting for i in s in back side doubt
print(l)

l=[7,3,2,5,1,5,6,4,8,4,5,1,9,4,1,2,5,9,6,]
rl=[0 if i%2==0 else i for i in l]
print(rl)

l=[7,3,2,5,1,5,6,4,8,4,5,1,9,4,1,2,5,9,6,]#set comphersiaon
rl=(0 if i%2==0 else i for i in l)
print(rl)

l=[7,3,2,5,1,5,6,4,8,4,5,1,9,4,1,2,5,9,6,]
rl={i:l.count(i) for i in l}
print(rl)
