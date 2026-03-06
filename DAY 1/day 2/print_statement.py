Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> b=20.9
>>> c="python"
>>> a
10
>>> b
20.9
>>> c
'python'
>>> print(a,b,c)
10 20.9 python
>>> print("a=",a,"b=",b,"c=",c)
a= 10 b= 20.9 c= python
>>> print("a=",a,"b=",b,"c=",c,sep='')
a=10b=20.9c=python
>>> #iif there is gap
>>> print("a=",a,"b=",b,"c=",c,sep='\n')
a=
10
b=
20.9
c=
python
>>> print("a=",a,"b=",b,"c=",c,sep='\n\n')
a=

10

b=

20.9

c=

python
>>> print("a=",a,"b=",b,"c=",c,sep='\n',end='\n\n')
a=
10
b=
20.9
c=
python

print("a=",a,"b=",b,"c=",c,sep='\n',end='.....')
a=
10
b=
20.9
c=
python.....
print(f"a={a},b={b},c={c}")
a=10,b=20.9,c=python
print(f"a= {a},b= {b},c= {c}")
a= 10,b= 20.9,c= python
print(f"a= {},b= {},c= {}".format(a,b,c))
SyntaxError: f-string: valid expression required before '}'
print("a= {},b= {},c= {}".format(a,b,c))
a= 10,b= 20.9,c= python
print("a=%d b=%f c=%s"%(a,b,c))
a=10 b=20.900000 c=python
print("a= {1},b= {2},c= {3}".format(a,b,c))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print("a= {1},b= {2},c= {3}".format(a,b,c))
IndexError: Replacement index 3 out of range for positional args tuple

print("a= {1},b= {2},c= {0}".format(a,b,c))
a= 20.9,b= python,c= 10
