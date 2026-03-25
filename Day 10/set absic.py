Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s={}
>>> type(s)
<class 'dict'>
>>> s=set()
>>> type(s)
<class 'set'>
>>> s={5678,74847,926,9287,716354,826}
>>> s
{716354, 926, 9287, 826, 5678, 74847}
>>> s.add(124)
>>> s
{716354, 926, 9287, 826, 124, 5678, 74847}
>>> s.remove(124)
>>> s
{716354, 926, 9287, 826, 5678, 74847}
>>> s
{716354, 926, 9287, 826, 5678, 74847}
>>> s
{716354, 926, 9287, 826, 5678, 74847}
>>> s.add(12.3)
>>> s
{716354, 926, 9287, 826, 12.3, 5678, 74847}
>>> s.add('string')
>>> s
{'string', 716354, 926, 9287, 826, 12.3, 5678, 74847}
>>> s.add(2+3j)
>>> s
{716354, 9287, (2+3j), 12.3, 926, 74847, 5678, 'string', 826}
>>> s.add(False)
>>> s
{False, 716354, 9287, (2+3j), 12.3, 926, 74847, 5678, 'string', 826}
>>> 
>>> s
{False, 716354, 9287, (2+3j), 12.3, 926, 74847, 5678, 'string', 826}
>>> s.add(1)
>>> s
{False, 1, 716354, 9287, (2+3j), 12.3, 926, 74847, 5678, 'string', 826}
>>> s.update({2,3,4})
>>> s
{False, 1, 716354, 2, 3, 4, 9287, (2+3j), 12.3, 926, 74847, 5678, 'string', 826}
>>> s.pop()
False
>>> s.pop()
1
s.pop()
716354
s
{2, 3, 4, 9287, (2+3j), 12.3, 926, 74847, 5678, 'string', 826}
s
{2, 3, 4, 9287, (2+3j), 12.3, 926, 74847, 5678, 'string', 826}
s.remove(3)
s
{2, 4, 9287, (2+3j), 12.3, 926, 74847, 5678, 'string', 826}
s.remove(3)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.remove(3)
KeyError: 3
s
{2, 4, 9287, (2+3j), 12.3, 926, 74847, 5678, 'string', 826}
s.discard(3)
s
{2, 4, 9287, (2+3j), 12.3, 926, 74847, 5678, 'string', 826}
for i in s:
    print(i)

    
2
4
9287
(2+3j)
12.3
926
74847
5678
string
826
a=[9,8,7,4,5,1]
b=[2,3,6,9]
a&b
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a&b
TypeError: unsupported operand type(s) for &: 'list' and 'list'
a & b
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a & b
TypeError: unsupported operand type(s) for &: 'list' and 'list'
a ={9,8,7,4,5,1}
b={2,3,6,9}
a&b
{9}
a|b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a-b
{1, 4, 5, 7, 8}
#{9}{7}{5}{6}{9,7}{7,5}{5,3}
{9}>a
False
{9}<a
True
a.isdisjoint(b)
False
{0}.isdisjoint(a)
True
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a.intersection(b)
{9}
s
{2, 4, 9287, (2+3j), 12.3, 926, 74847, 5678, 'string', 826}
a
{1, 4, 5, 7, 8, 9}
len(A)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    len(A)
NameError: name 'A' is not defined. Did you mean: 'a'?
len(a)
6
max(a)
9
min(a)
1
sorted(a)
[1, 4, 5, 7, 8, 9]
's'.islower()
True
'w'.isupper()
False
'123'.isupper()
False
'@!'.islower()
False
'123'.isdigit()
True

= RESTART: C:/Users/tejav/OneDrive/Desktop/PFS COURSE RE 1/Day 10/password check.py
enter the password: 12345
weak password

= RESTART: C:/Users/tejav/OneDrive/Desktop/PFS COURSE RE 1/Day 10/password check.py
enter the password: 
= RESTART: C:/Users/tejav/OneDrive/Desktop/PFS COURSE RE 1/Day 10/password check.py
enter the student name: venkat
Traceback (most recent call last):
  File "C:/Users/tejav/OneDrive/Desktop/PFS COURSE RE 1/Day 10/password check.py", line 35, in <module>
    sum =data[name]['python']+data[name]['mysql']+data[name]['django']
KeyError: 'python'

= RESTART: C:/Users/tejav/OneDrive/Desktop/PFS COURSE RE 1/Day 10/password check.py
enter the student name: venkat
venkat,you got first class

= RESTART: C:/Users/tejav/OneDrive/Desktop/PFS COURSE RE 1/Day 10/password check.py
enter the student name: 
= RESTART: C:/Users/tejav/OneDrive/Desktop/PFS COURSE RE 1/Day 10/password check.py
enter the student name: haribabu
haribabu,you have not returned the exam. please bring your parents
