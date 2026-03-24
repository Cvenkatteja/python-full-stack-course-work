data = {
    '123456':{'pin':'1234','balance':4000,'history':[]},
    '123456':{'pin':'1234','balance':9000,'history':[]},
    '123456':{'pin':'1234','balance':8000,'history':[]},
    '123456':{'pin':'1234','balance':6000,'history':[]},
    }

def deposit(acc_num):
    print("----------------------------------")
    amount =int(input("enter the amount: "))
    data[acc_num]['balance']+=amount
    print(f"{amount}is added succeessfully")
    check_balance(acc_num)
    data[acc_num]['history'].append(f"{amount}is deposited")
    print("-----------------------------------")
    
def withdraw(acc_num):
    print("----------------------------------")
    amount =int(input("enter the amount :"))
    if data[acc_num]['balance']>=amount:
        data[acc_num]['balance']-=amount
        print(f"{amount}is withdrawn successfully")
        check_balance(acc_num)
        data[acc_num]['history'].append(f"{amount}is withdrawn")
        print("----------------------------------")
    else:
        print("insufficient balance")
        
def change_pin(acc_num):
    pass

def check_balance(acc_num):
    print("----------------------------------")
    print(f"current balance:{data[acc_num]['balance']}")
    print("--------------------------------------")
    
def view_transaction(acc_num):
    if data[acc_num]['history']:
        print("---------transaction history------------")
        for i in data[acc_num]['history']:
            print(i)
        else:
            print("-----------end of transcation------------")
    else:
        print("no taranscation")
def menu():
    print("[C]heck balance")
    print("[D]eposit")
    print("[W]ithdraw")
    print("[V]iew_transcation")
    print("change [P]in")
    print("[E]xit")
    
print("------------welcome to the atm-------------")
acc_num=input("enter the account number: ")
pin=input("enter the pin number :")

if acc_num in  data and data[acc_num]['pin']==pin:
    print("login succeessfull ")
    while True:
        menu()
        ch= input("enter your choice :")
        if ch=='c':
            check_balance(acc_num)
        elif ch=='d':
            deposit(acc_num)
        elif ch=='w':
            withdraw(acc_num)
        elif ch=='v':
            view_transaction(acc_num)
        elif ch=='p':
            change_pin(acc_num)
        elif ch=='e':
            print("----------exit--------")
            break
        else:
            print("enter the valid choice")
else:
    print("invalid login")    
            
            
