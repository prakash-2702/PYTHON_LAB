
user={} #To store user's info
blocked_account=[] #Blocked account

class bank:
    def __init__(self,name,account,mobile,address,pin,balance):
        self.name=name
        self.pin=pin
        self.balance=balance
        self.account=account
        self.mobile=mobile
        self.address=address
    
    def account_info(self):
        print("Name:" ,self.name)
        print("Mobile Number:",self.mobile)
        print("Account Number:",self.account)

    def Pin_change(self):
        while(True):
            new_pin=input("Enter new PIN ")
            pin_to_check=input("Enter new PIN ")
            if new_pin==pin_to_check:
                self.pin=new_pin
                print("PIN changed succesfully")
                break
            else:
                print("Try Again")
                continue
    
    def withdrawal(self):
        while(True):
            amount=int(input("Enter the amount to withdraw "))
            if amount>self.balance:
                print("Not enough balance")
                continue
            elif amount<=self.balance:
                self.balance-=amount
                print("Withdrawal successfull")
                print("Account balance:",self.balance)
                break

    def deposit(self):
        amount=int(input("Enter the amount to deposit "))
        self.balance+=amount
        print("Deposit successfull")
        print("Account balance:",self.balance)
    
    def balance_enquiry(self):
        print("Name:" ,self.name)
        print("Account Number:",self.account)
        print("Account Balance:",self.balance)
    
    
user["8045762845"]=bank("Prakash","8045762845","9076537382","Bhandup","1111",2000)
user["8456245360"]=bank("Parth","8456245360","9136486573","Kandivali","2222",1000)
user["8097654321"]=bank("Abhishekh","8097654321","9345627890","Kalyan","3333",7000)
user["8765098765"]=bank("Vikas","8765098765","9364785643","Bandra","4444",2800)
user["8056789045"]=bank("Akash","8056789045","9465837393","Delhi","5555",12000)

def new_user_info():
    name=input("Enter name ")
    account=input("Enter account number ")
    mobile=input("Enter mobile number ")
    address=input("Enter address ")
    pin=input("Enter pin ")
    balance=0
    if(len(acc_no)==10 and len(mobile)==10 and len(pin)==4):
        user[account]=bank(name,account,mobile,address,pin,balance)
    else:
        print("\nEnter valid information")

def service(option):
    flag=3
    account=input("Enter the account number ")
    if account in blocked_account:
        print("Your account is blocked\nContact bank for more details")
    while(True):
        pin_no=input("Enter the PIN ")
        if pin_no==user[account].pin:
            if option=="account_info()":
                user[account].account_info()
                break
            if option=="Pin_change()":
                user[account].Pin_change()
                break
            if option=="balance_enquiry()":
                user[account].balance_enquiry()
                break
            if option=="withdrawal()":
                user[account].withdrawal()
                break
            if option=="deposit()":
                user[account].deposit()
                break
        else:
            flag-=1
            if flag==0:
                print("Oops! Your account is now blocked")
                blocked_account.append(account)
                break
            print("Try again\ntries left:",flag)
            continue

while(True):
    choice=int(input("\nEnter choice\n0.Quit\n1.New User\n2.Account Info\n3.PIN Change\n4.Balance Enquiry\n5.Withdraw Money\n6.Deposit Money\n"))
    service_option=["Quit","New_User","account_info()","Pin_change()","balance_enquiry()","withdrawal()","deposit()"]
    if (service_option[choice])=="Quit":
        print("Thanks for visiting")
        break
    
    elif (service_option[choice])=="New_User":
        new_user_info()

    else:
        service(service_option[choice])

        
    
