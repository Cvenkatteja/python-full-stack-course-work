Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name=input()
pyhton
name
'pyhton'
type(name)
<class 'str'>
names =input("enter the name:")
enter the name:venkat
names
'venkat'
type(names)
<class 'str'>
age=input("enter the age:")
enter the age:24
type(age)
<class 'str'>
age=int(input("enter the age :"))
enter the age :56
type(age)
<class 'int'>
price=input("enter the price:")
enter the price:56.77
price
'56.77'
price=int(input("enter the price:"))
enter the price:56.97
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    price=int(input("enter the price:"))
ValueError: invalid literal for int() with base 10: '56.97'
price=float(input("enter the price:"))
enter the price:89.67
price
89.67
type(price)
<class 'float'>
'venkat,teja,raja'
'venkat,teja,raja'
names=input('enter the name:')
enter the name:venkat,teja,raja
names
'venkat,teja,raja'
type(names)
<class 'str'>
names=input('enter the name').split()
enter the namevenkat raja
names
['venkat', 'raja']
#we need use the list means.spilt
hanger=input('enter the hanges')
enter the hanges
hanger=input('enter the hanges').spilt('....')
enter the hangesnumbs,bangers,interes
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    hanger=input('enter the hanges').spilt('....')
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
hanger=input('enter the hanges').split('...')
enter the hangesnumbs,bangers,interes
hanger
['numbs,bangers,interes']
numbers=input('enter the num:').split()
enter the num:1,4,6,9,7
numbers
['1,4,6,9,7']
type(numbers)
<class 'list'>
numbers=list(map(int,input('enter the number:').split()))
enter the number:24,4,5,8,9
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    numbers=list(map(int,input('enter the number:').split()))
ValueError: invalid literal for int() with base 10: '24,4,5,8,9'
numbers=list(map(int,input("enter the number:").split()))
enter the number:2 3 4 6 7 8 9
numbers
[2, 3, 4, 6, 7, 8, 9]
type(numbers)
<class 'list'>
numbers=lsit(map(float,input("enter the numbers:").split()))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    numbers=lsit(map(float,input("enter the numbers:").split()))
NameError: name 'lsit' is not defined
numbers=list(map(float,input("enter the numbers:").split()))
enter the numbers:89.7 2.2 4.5
numbers
[89.7, 2.2, 4.5]
numbers=tuple(map(int,input("enter the number:").split()))
enter the number:3 8 9 7 5 
numbers
(3, 8, 9, 7, 5)
prices=tuple(map(float,input("enter the price:").split()))
enter the price:23 77 890
prices
(23.0, 77.0, 890.0)
levels=set(map(int,input("enter the levels:").spilt()))
enter the levels:45 7 9 99
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    levels=set(map(int,input("enter the levels:").spilt()))
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
levels=set(map(int,input("enter the levels:").split()))
enter the levels:45 7 899 4
levels
{899, 4, 45, 7}
levels=set(map(float,input("enter the levels:").split()))
enter the levels:67 9 999 5 
levels
{9.0, 67.0, 5.0, 999.0}
type(levels)
<class 'set'>
h=eval(input("enter the number:" ))
enter the number:{2:3,2:4,6:7}
h
{2: 4, 6: 7}
k=eval(input("enter the numbers:"))
enter the numbers:[3,4,5,6,6,7]
k
[3, 4, 5, 6, 6, 7]
#we can take any data type with eval function
a,b,c=10,220,30
a
10
b
220
c
30
a=b=c=10
a
10
b
10
c
10
a,b=b,a
a
10
b
10
username password ='ven;kat''pya13u4'
SyntaxError: invalid syntax
username,password ='ven;kat''pya13u4'
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    username,password ='ven;kat''pya13u4'
ValueError: too many values to unpack (expected 2)
username,password ='ven;kat','pya13u4'
username
'ven;kat'
password
'pya13u4'
username,password=input("enter the username and password:").split()
enter the username and password:venkat,bang35;6
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    username,password=input("enter the username and password:").split()
ValueError: not enough values to unpack (expected 2, got 1)
username,password=input("enter the username and password:").split()

enter the username and password:venkat numbe3678
username
'venkat'
password
'numbe3678'
username,password=input("enter the username and password:").spilt()
enter the username and password:
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    username,password=input("enter the username and password:").spilt()
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
username,password=input("enter the username and password:").split()
enter the username and password:banger hemanth
username
'banger'
password
'hemanth'
a,b,c=list(map(int,input("enter the number:").split()))
enter the number:2 4 6 
a
2
b
4
c
6
#operaters
a+b
6
a-b
-2
a*b
8
a/b
0.5
a//b
0
a%b
2
a**b
16
a**2
4
b**4
256
#comprasion opertaors
a=10
b=5
a<b
False
a>b
True
a<=b
False
a>=b
True
a!=b
True
a==b
False
#relation operators
#assignment operators
a=10
b=20
a=a+10
a
20
a+=10
a
30
a=-10
a
-10
a-=10
a
-20
a=a*10
a=
SyntaxError: invalid syntax
a
-200
a*=2
a
-400
a=a/10
a
-40.0
a/=10
a
-4.0
b/=20
b
1.0
#logical opraters
6%2==0 and7%3==0
SyntaxError: invalid syntax
6%2==0 and 7%4==0
False
7%7==0
True
not 7%4==0
True
not 8*4==0
True
8%9==0 or 8%3==0
False
#membership operator
n='venkat'
e in n
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    e in n
NameError: name 'e' is not defined
'e' in n
True
't 'in n
False
't' in n
True
# meber ship will check in number if its word in spelling or not
t=[1,2,3,5 ]
2 in t
True
4 in t
False
3 in t
True
7 not in t
True
d={1:2,4:6,6:7}
4 in d
True
25 in d
False
77 not in d
True
6 in d
True
#identity operator
a=[1,2,3,4,5,6]
b=[1,2,3,4,5,6]
a==b
True
a is b
False
c=a
c
[1, 2, 3, 4, 5, 6]
c==a
True
>>> a is c
True
>>> id(a)
2450661948736
>>> id(b)
2450661944960
>>> id(c)
2450661948736
>>> a.append(9)
>>> a
[1, 2, 3, 4, 5, 6, 9]
>>> id(a)
2450661948736
>>>  s='python'
...  
SyntaxError: unexpected indent
>>> s='python'
>>> id(s)
2450617188000
>>> #bitwise operator
>>> 1 -0001
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> & |^ ~ << >>
SyntaxError: invalid syntax
>>> 10 & 21
0
>>> 3|4
7
>>> 34^67
97
>>> 22~45
SyntaxError: invalid syntax
>>> ~2
-3
>>> ~66
-67
>>> 10<<2
40
>>> 2>>1
1
>>> 2<<2
8
>>> 2>>2
0
