'''def add(a,b):
    return a+b
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print("sum=",add(a,b))'''

'''exp = input()
if '+' in exp:
    a,b=exp.split("+")
    print(add(int(a),int(b))
elif  '-' in exp:
    a,b=exp.split("-")
    print(add(int(a),int(b))
elif '*' in exp:
    a,b=exp.split("*")
    print(add(int(a),int(b))
elif '%' in exp:
    a,b=exp.split("%")
    print(add(int(a),int(b))          
elif'/' in exp:
    a,b=exp.split("/")
    print(add(int(a),int(b))'''            
        
#list
'''i=[]
i=list[]
a=[1,2,3]
b=[1,2,3]
a+b
a*b          
names=['venkat','sujit','hemanth','sai']
names
names[:2]
names[1:]
'venkat' in names
'hemanth' not in names
 a,b,c=[10,20,30]
a
b         
c
a,b,c,d=['venkat','hemanth','raja','prabhu']
a
b
c
d
names
names[1]
names.append['manjo']
names.append['neha']
names.extend(['venkat','babu','janu'])
names.insert(1,"prasasna")#if u insert we needto giv indexing
names.pop()
names.pop(1)
names.del()
names.del(1)
names.clear()
del.names(1)
names.remove(1)
len(1)
min(1)
sorted(2)
l.sort()
max(names)'''
products = [['laptop',50000],
            ['iphone',89000],
            ['batttery',56000],
            ['tv',67000]
            ]
def view_products():
    print('products_name'.ljust(15,'-'),'prices')
    for i  in products:
        print(i[0].ljust(15,'-'),i[1])
def add_products():
    product_name=input("enter the  product name:")
    prices=int(input("enter the price:"))
    products.append([product_name,prices])
    print(f"{product_name}is added")
def del_product():
    product_id=int(input("enter the product id:"))
    print(f"{products[product_id]} is deleted")
    products.pop(product_id)
while True:
    print ("welcome to the flipkart \n",end="-")
    print("1.view_products")
    print("2.add_products")
    print("3.del_products")
    print("4.exit")

    ch=int(input("enter your choice:"))
    if ch==1:
        view_products()
    elif ch==2:
        add_products()
    elif ch==3:
        del_products()
    else:
        print("exit  hht esytems:")
        break

    
          
