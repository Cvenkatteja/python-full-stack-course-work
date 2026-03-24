Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> d={}
>>> \
... 
... type(d)
<class 'dict'>
>>> d
{}
>>> s=set()
>>> data = {'name':'venkat','age':21,'course':'pfs','skills':['pyhton','java','c']}
>>> data
{'name': 'venkat', 'age': 21, 'course': 'pfs', 'skills': ['pyhton', 'java', 'c']}
>>> data
{'name': 'venkat', 'age': 21, 'course': 'pfs', 'skills': ['pyhton', 'java', 'c']}
>>> data['name']
'venkat'
>>> data['age']
21
>>> data['course']
'pfs'
>>> d={}
>>> data['skills']
['pyhton', 'java', 'c']
>>> d[1]="int"
>>> d
{1: 'int'}
>>> d[1.1]='float'
>>> d
{1: 'int', 1.1: 'float'}
>>> d['dfghd']='string'
>>> d
{1: 'int', 1.1: 'float', 'dfghd': 'string'}
>>> d[True]
'int'
>>> 'bool
SyntaxError: unterminated string literal (detected at line 1)
>>> d[True]
'int'
>>> d[True]='bool']
SyntaxError: unmatched ']'
>>> d[True]='bool'
>>> d
{1: 'bool', 1.1: 'float', 'dfghd': 'string'}
d[2+3j]='complex'
d
{1: 'bool', 1.1: 'float', 'dfghd': 'string', (2+3j): 'complex'}
d[(1,2,3)]='tuple'
d
{1: 'bool', 1.1: 'float', 'dfghd': 'string', (2+3j): 'complex', (1, 2, 3): 'tuple'}
d[{1,2,3}]='set'
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    d[{1,2,3}]='set'
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
d[{1:1}]='dict'
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d[{1:1}]='dict'
TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
d
{1: 'bool', 1.1: 'float', 'dfghd': 'string', (2+3j): 'complex', (1, 2, 3): 'tuple'}
d['name']='teja'
d
{1: 'bool', 1.1: 'float', 'dfghd': 'string', (2+3j): 'complex', (1, 2, 3): 'tuple', 'name': 'teja'}
s
set()
d
{1: 'bool', 1.1: 'float', 'dfghd': 'string', (2+3j): 'complex', (1, 2, 3): 'tuple', 'name': 'teja'}
id(d)
2537304952960
d['age']=21
d
{1: 'bool', 1.1: 'float', 'dfghd': 'string', (2+3j): 'complex', (1, 2, 3): 'tuple', 'name': 'teja', 'age': 21}
d['age']=21
id(d)
2537304952960
d['name']
'teja'
d['name']='himaj'
d
{1: 'bool', 1.1: 'float', 'dfghd': 'string', (2+3j): 'complex', (1, 2, 3): 'tuple', 'name': 'himaj', 'age': 21}
d.items()
dict_items([(1, 'bool'), (1.1, 'float'), ('dfghd', 'string'), ((2+3j), 'complex'), ((1, 2, 3), 'tuple'), ('name', 'himaj'), ('age', 21)])
d.keys()
dict_keys([1, 1.1, 'dfghd', (2+3j), (1, 2, 3), 'name', 'age'])
d.values()
dict_values(['bool', 'float', 'string', 'complex', 'tuple', 'himaj', 21])
len(d)
7
sorted(d)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    sorted(d)
TypeError: '<' not supported between instances of 'str' and 'float'
d.values()
dict_values(['bool', 'float', 'string', 'complex', 'tuple', 'himaj', 21])
sorted(data)
['age', 'course', 'name', 'skills']
max(data)
'skills'
min(data)
'age'
data
{'name': 'venkat', 'age': 21, 'course': 'pfs', 'skills': ['pyhton', 'java', 'c']}
data['k1']='v1'
data
{'name': 'venkat', 'age': 21, 'course': 'pfs', 'skills': ['pyhton', 'java', 'c'], 'k1': 'v1'}
data.update({'v1':'t2','b1':'n1'})
data
{'name': 'venkat', 'age': 21, 'course': 'pfs', 'skills': ['pyhton', 'java', 'c'], 'k1': 'v1', 'v1': 't2', 'b1': 'n1'}
del.data['k1']
SyntaxError: invalid syntax
del data['k1']
data
{'name': 'venkat', 'age': 21, 'course': 'pfs', 'skills': ['pyhton', 'java', 'c'], 'v1': 't2', 'b1': 'n1'}
data.popitem()
('b1', 'n1')
data
{'name': 'venkat', 'age': 21, 'course': 'pfs', 'skills': ['pyhton', 'java', 'c'], 'v1': 't2'}
data.popitem()
('v1', 't2')
data
{'name': 'venkat', 'age': 21, 'course': 'pfs', 'skills': ['pyhton', 'java', 'c']}
data.pop('name')
'venkat'
data.pop('age')
21
data
{'course': 'pfs', 'skills': ['pyhton', 'java', 'c']}
data.clear()
data
{}
print("------------welcome to the atm-----------")
------------welcome to the atm-----------

===== RESTART: C:/Users/tejav/OneDrive/Desktop/PFS COURSE RE 1/Day 9/atm.py ====
------------welcome to the atm-------------
enter the account number: 
===== RESTART: C:/Users/tejav/OneDrive/Desktop/PFS COURSE RE 1/Day 9/atm.py ====
------------welcome to the atm-------------

enter the account number: 
===== RESTART: C:/Users/tejav/OneDrive/Desktop/PFS COURSE RE 1/Day 9/atm.py ====
------------welcome to the atm-------------
enter the account number: 
===== RESTART: C:/Users/tejav/OneDrive/Desktop/PFS COURSE RE 1/Day 9/atm.py ====
------------welcome to the atm-------------
enter the account number: 
===== RESTART: C:/Users/tejav/OneDrive/Desktop/PFS COURSE RE 1/Day 9/atm.py ====
------------welcome to the atm-------------
enter the account number: 
===== RESTART: C:/Users/tejav/OneDrive/Desktop/PFS COURSE RE 1/Day 9/atm.py ====
------------welcome to the atm-------------
enter the account number: 
===== RESTART: C:/Users/tejav/OneDrive/Desktop/PFS COURSE RE 1/Day 9/atm.py ====
------------welcome to the atm-------------
enter the account number: 
===== RESTART: C:/Users/tejav/OneDrive/Desktop/PFS COURSE RE 1/Day 9/atm.py ====
------------welcome to the atm-------------
enter the account number: 
===== RESTART: C:/Users/tejav/OneDrive/Desktop/PFS COURSE RE 1/Day 9/atm.py ====
------------welcome to the atm-------------
enter the account number: 
===== RESTART: C:/Users/tejav/OneDrive/Desktop/PFS COURSE RE 1/Day 9/atm.py ====
------------welcome to the atm-------------
enter the account number: 123456
enter the pin number :1234
login succeessfull 
[C]heck balance
[D]eposit
[W]ithdraw
[V]iew_transcation
change [P]in
[E]xit
enter your choice :c
----------------------------------
current balance:6000
--------------------------------------
[C]heck balance
[D]eposit
[W]ithdraw
[V]iew_transcation
change [P]in
[E]xit
enter your choice :d
----------------------------------
enter the amount: 4599
4599is added succeessfully
----------------------------------
current balance:10599
--------------------------------------
-----------------------------------
[C]heck balance
[D]eposit
[W]ithdraw
[V]iew_transcation
change [P]in
[E]xit
enter your choice :c
----------------------------------
current balance:10599
--------------------------------------
[C]heck balance
[D]eposit
[W]ithdraw
[V]iew_transcation
change [P]in
[E]xit
enter your choice :w
----------------------------------
enter the amount :6000
6000is withdrawn successfully
----------------------------------
current balance:4599
--------------------------------------
----------------------------------
[C]heck balance
[D]eposit
[W]ithdraw
[V]iew_transcation
change [P]in
[E]xit
enter your choice :c
----------------------------------
current balance:4599
--------------------------------------
[C]heck balance
[D]eposit
[W]ithdraw
[V]iew_transcation
change [P]in
[E]xit
enter your choice :
===== RESTART: C:/Users/tejav/OneDrive/Desktop/PFS COURSE RE 1/Day 9/atm.py ====
------------welcome to the atm-------------
