'''def fun():
    if base_con:
        return
    fun()'''

'''def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
display(1)'''

'''def display(n):
    if n>10:
        return
    
    display(n+1)
    
    print(n)
    
display(1)'''   
'''def display(n):
    if n>10:
        return
    print("before",n)
    display(n+1)
    print("after",n)
display(1)'''

'''def display(s,i):
    if i==len(s):
        return
    print(s[i])
    display(s,i+1)
display("python programming",0)'''    
        
    
'''def display(h,i):
    if i==len(h):
        return
    print(h[i])
    display(h,i+1)
display("venkat teja",0)'''

'''def display(s,i):
    if i==len(s):
        return
    print(s[:i+1])
    display(s,i+1)
display("python programming",0)'''    

'''def display(s,i):
    if i<=0:
        return
    display(s,i-1)
    print(s*i)
display("abc",5)'''
'''def display(s,i,n):
    if i==len(s)-n:
        return
    print(s[i:i+n])
    display(s,i+1,n)
display("aasdfghjkl",0,3)'''
'''def display(s,n,i):
    if n==len(s)-i:
        return
    print(s[n:n+i])
    display(s,n+1,i)
display("asdfghjklfghj",0,3)'''
'''def display(l,i,sum):
    if i==len(l):#dobut
        return sum
    display(l,i+l,sum+l[i])
print(display([1,2,3,4,5,6,7,8,9,0],0,0))'''
#pass by value
#int,float,str,list,tuple,set,dic
def display(n):
    n=n+(2,1,4)
    print("inside",n)
    
n=(1,2,3,4)
display(n)
print("outside",n)



