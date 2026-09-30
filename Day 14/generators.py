def reels():
    r=['1..100','101..200','201..300','301..400','401..500']
    for i in r:
        yield i

scroll = reels()

print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))


def display():
    yield"pfs-50"
    yield"pfs-40"
    yield"pfs-67"
    yield"pfs-18"
    yield"pfs-45"
    yield"pfs-15"


leave = display()

print(next(leave))
print(next(leave))
print(next(leave))
print(next(leave))
print(next(leave))

n=7
for  i in range(n):
    if i<=n//2:
        for j in range(i+1):
            print("*",end=" ")
        print()
    else:
        for s in range(i-n):
            print("",end=" ")                
    
