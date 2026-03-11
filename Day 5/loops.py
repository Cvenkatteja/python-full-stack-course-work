'''products = {'bread','butter','milk','sugar','salt'}
for item in products:
    print(item)'''

'''    
products = {'bread':50,'butter':40,'milk':59,'sugar':78,'salt':90}
for items in products:
    print("products name:",items)
    print("product price:",products[items])
    print("buy now add to cart")
    print("add to favourite")
    print(".......................")'''
    
pin =1234
for i in range(5):
    user_pin =int(input("enter the pin: "))
    if user_pin == pin:
        print("login succeessfully")
        break
    else:
        print("invalid password,try agian")
else:
    print("you have reached the max input")
        
