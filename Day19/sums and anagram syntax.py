'''
1.armstrong
2.anagram
3.fibanonice
4.factorial
5.strong num
6.first non-rep char
7.reverse
8.palindrone
9.sum of digits
10.lenof num
'''
#9
'''n=int(input("enter the  input: "))

sum=0

while n>0:
    sum+=n%10
    n//=10
print(sum)'''

#10
'''
n=int(input("enter the input :"))

cnt=0
while n>0:
    cnt+=1
    n//=10
print(cnt)    
'''     
    
#7
'''
n=int(input("enter the input : "))

rev = 0
while n>0:
    rev=rev*10+n%10
    n//=10
print(rev)
'''
#8
'''
n=int(input("enter the input :"))

num=n
rev=0
while n>0:
    rev=rev*10+ n%10
    n//=10
    
if num==rev:
    print(" palindrone")
else:
    print(" not paliandorne")
'''
#4
'''
n=int(input("enter the input: "))

fact=1

for i in range(n,0,-1):
    fact =fact *i
print(fact)
'''
#2
'''
s1,s2=int(input("enter the input: " )).split()
if sorted(s1)==sorted(s2):
    print("angram")
else:
    print("not angram")
'''
#6
'''
s=input("enter the string : ")
for  i in s:
    if s.count(i)==1:
        print(i)
        break
else:
    print("all are repeating char")
'''
#3
'''
a=0
b=1
n=int(input("enter the input: "))

for i in range(n-2):
    c=a+b
    print(c,end=' ')
    a=b
    b=c
'''
#1
'''
n=int(input("enter the input: "))
num=n
arm =0

while n>0:
    arm+=(n%10)**3
    n//=10
if num==arm:
    print("is armstrong")
else:
    print("not armstrong")
'''

n=int(input("enter the numbers: "))
for i in range(1,n):
    if n%i==0:
        print(i)


































    
    
        

    


    

    


























































    





























