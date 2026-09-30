#open-read| write| apppend -Close

'''try:
    file =open('student.txt,'r')
#except fileNotFoundError:
 #   print("file not found: ")
else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readline())
    file.close()'''

'''file=open("student.txt",'r')
print(file.read())'''
'''
try:
    file =open('student.txt','r')
except fileNotFoundError:
    print("file not found: ")
else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()
'''

with open('student.txt','a')as file:
    file.write('\nsujitbhanu')
    file.write('\nveersha')
    #file.seek(0)
    #print(file.read())
