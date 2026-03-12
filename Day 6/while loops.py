'''
ini
while condi:
upd
#stmts
'''
'''
i=1
while i<=10:
    print(i)
    i+=1
'''
'''
i=20
while i<=30:
    print(i)
    i+=1
'''
'''
i=20
while i <=30:
    if i==25:
        break #continue also same anf for pass also same
    print(i)
    i+=1
'''
'''
bullets=10
while bullets >0:
    print(f"{bullets} bullets are left,you ;can shoot")
    bullets-=1
else:
    
    print("the bullets are over")
  '''
'''
moves=20
while moves >0:
    print(f"{moves}there is only onee left")
    moves-=1
else:
    print("the end of the string")
'''
'''
moves = 10
winning_point=4
while moves>0:
    if winning_point==moves:
        print("you with the game!!")
        break
    print(f"{moves} the moves are over")
    moves-=1
else:
    print("the game is over")
'''
''''
data ={}
n=int(input("enter the  no of students :"))
for i in range (n):
    name= input("enter the name:")
    data[name]=false
    print(data)   
'''
'''
data ={}
n=int(input("enter the  no of students :"))
for i in range (n):
    name= input("enter the name:")
    data[name]=False
    
for name in data:
    status =int(input(f"{name}the attendence status(0-Absent,1-Present):"))
    data[name]=bool(status)
print(data)    
'''
#string
s="python"
print("s")
s='''python'''
print('s')
s+'python'
print('s+')
s*10
'09872'*12
"*"*10
s='python'
s[4]
s[3]
s[-2]
names='manjo venkat  rajesh babu'
names[:8]
names[10:15]
names[::5]
names[-2:-6]
'venkat' in names
'venkat' not in names
len(names)
max(names)
min(names)
chr(n89)
ord("a")
sorted(names)
names.rplace("venkat","manideep")
names.spilt()
s.center(50,"=")
s.ljust(30,"+")
s.rjust(20,"+")


      
    

        

