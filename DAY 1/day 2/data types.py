Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
followers=2000
followers
2000
type(followers)
<class 'int'>
subcribers=2.899k
SyntaxError: invalid decimal literal
subcribers=2.899
subcribers
2.899
type(subcribers)
<class 'float'>
price=3.987
price
3.987
type(price)
<class 'float'>
a=5+8j
a
(5+8j)
type(a)
<class 'complex'>
b=1+45J
b
(1+45j)
type(b)
<class 'complex'>
s='python'
s
'python'
type("class")
<class 'str'>
type(s)
<class 'str'>
consumer_product="machines"
consumer_product[1]
'a'
consumer_product[0]
'm'
KeyboardInterrupt
consumer_product[5]
'n'
consumer_product[6]
'e'
list=['venkat','sumit','ramesh']
list
['venkat', 'sumit', 'ramesh']
list[0]
'venkat'
list[2]
'ramesh'
list[1]
'sumit'
# the list can include the duplicates
list.append('manjo')
list
['venkat', 'sumit', 'ramesh', 'manjo']
list.append('manjo')
list
['venkat', 'sumit', 'ramesh', 'manjo', 'manjo']
#tuple
t=(1,2,3,4,5,6,7)
t
(1, 2, 3, 4, 5, 6, 7)
type(t)
<class 'tuple'>
#set
set={1356,venkat,7869}
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    set={1356,venkat,7869}
NameError: name 'venkat' is not defined
set={12389,89676,536}
set
{536, 89676, 12389}
type(set)
<class 'set'>
#in set we can't add  we can delete or add
#dictionary
products={"product
          
SyntaxError: unterminated string literal (detected at line 1)
products={"product_id":1,"product_name":battery,"price":4002}
          
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    products={"product_id":1,"product_name":battery,"price":4002}
NameError: name 'battery' is not defined

products={"product_id":1,"product_name":"battery","price":4002}
          
products
          
{'product_id': 1, 'product_name': 'battery', 'price': 4002}
status = true
          
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    status = true
NameError: name 'true' is not defined. Did you mean: 'True'?
status= True
          
type(status)
          
<class 'bool'>
type(products)
          
<class 'dict'>
a=None
          
a
          
a=10
          
float(a)
          
10.0
str(a)
          
'10'
complex(a)
          
(10+0j)
list(a)
          
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    list(a)
TypeError: 'list' object is not callable
tuple(a)
          
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
bool(a)
          
True
a=12.7
          
int(a)
          
12
str(a)
          
'12.7'
complex(a)
          
(12.7+0j)
list(a)
          
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    list(a)
TypeError: 'list' object is not callable
bool(a)
          
True
a=12+4j
          
int(a)
          
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(a)
          
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
str(a)
          
'(12+4j)'
list(a)
          
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    list(a)
TypeError: 'list' object is not callable
tuple(a)
          
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    tuple(a)
TypeError: 'complex' object is not iterable
dict(a)
          
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    dict(a)
TypeError: 'complex' object is not iterable
set(a)
          
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    set(a)
TypeError: 'set' object is not callable
bool(a)
          
True
 a=[1,2,4,6,7,8,]
          
SyntaxError: unexpected indent
a=[1,2,4,6,7,8,]
          
int(a)
          
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(a)
          
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'list'
complex(a)
          
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    complex(a)
TypeError: complex() argument must be a string or a number, not list
tuple(a)
          
(1, 2, 4, 6, 7, 8)
set(a)
          
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    set(a)
TypeError: 'set' object is not callable
set(a)
          
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    set(a)
TypeError: 'set' object is not callable
set{a}
          
SyntaxError: invalid syntax
set(a)
          
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    set(a)
TypeError: 'set' object is not callable
bool(a)
          
True
t=(1,2,3,4)
          
int(t)
          
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
          
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
set(t)
          
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    set(t)
TypeError: 'set' object is not callable
set(t)
          
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    set(t)
TypeError: 'set' object is not callable
set (t)
          
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    set (t)
TypeError: 'set' object is not callable
tuple(t)
          
(1, 2, 3, 4)
dict(t)
          
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(t)
          
True
#set
          
s={1,2,4,5,6,7,8,9}
          
type(s)
          
<class 'set'>
int(s)
          
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
          
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
tuple(s)
          
(1, 2, 4, 5, 6, 7, 8, 9)
list(s)
          
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    list(s)
TypeError: 'list' object is not callable
bool(s)
          
True
d={1: 1,2: 2,3:9}
          
int(d)
          
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
          
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
>>> str(d)
...           
'{1: 1, 2: 2, 3: 9}'
>>> list(d)
...           
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    list(d)
TypeError: 'list' object is not callable
>>> tuple(d)
...           
(1, 2, 3)
>>> set(d)
...           
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    set(d)
TypeError: 'set' object is not callable
>>> my_set(d)
...           
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    my_set(d)
NameError: name 'my_set' is not defined
>>> bool(d)
...           
True
>>> a= True
...           
>>> int(a)
...           
1
>>> float(a)
...           
1.0
>>> list(a)
...           
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    list(a)
TypeError: 'list' object is not callable
>>> bool(a)
...           
True
