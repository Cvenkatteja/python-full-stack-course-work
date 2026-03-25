'''password = input("enter the password: ")
check=set()
if len(password)>=8:
    for i in  password:
        if i .islower():
            check.add('l')
        elif i.isupper():
            check.add('u')
        elif i.isdigit():
            check.add('n')
        else:
            check.add('s')

    if len(check)==4:
        print("strong password")
    else:
        print("weak password")
else:
    print("weak password")'''
     
#student report

data={
    'venkat':{'status':True,'python':89,'mysql':99,'django':99},
    'ramu':{'status':True,'python':59,'mysql':92,'django':89},
    'manjo':{'status':True,'python':48,'mysql':73,'django':68},
    'srinu':{'status':True,'python':83,'mysql':64,'django':76},
    'haribabu':{'status':True,'python':18,'mysql':15,'django':20},
    'santhosh':{'status':False,'python':None,'mysql':None,'django':None},
    'siva':{'status':True,'python':24,'mysql':56,'django':46}
    }
name=input("enter the student name: ")
if name in data:
    if data[name]['status']:
        sum =data[name]['python']+data[name]['mysql']+data[name]['django']
        avg=sum/3
        if avg>=90:
            print(f"{name},you got first class")
        elif avg>=75:
            print(f"{name},wish you all the best for next time")
        elif avg>=50:
            print(f"{name},need imporvement")
        elif avg>=35:
            print(f"{name},you failed  bring your parents")
        else:
            print(f"{name},you have not returned the exam. please bring your parents")
    else:
        print(f"{name},bring your father immeaditly")
else:
    print(f"{name} data is not found")
