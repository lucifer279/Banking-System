

# Banking System OOPS
#
# Creating Parent Class User
# Adding Details of User
# Creating Function to show user details


#Parent Class

class User():
    def __init__(self,branch,name,age,gender,ac_no):
        self.branch = branch
        self.name = name
        self.age = age
        self.gender = gender
        self.ac_no = ac_no


    def User_Details(self):

        print("")
        print("Branch - ",self.branch)
        print("Name - ",self.name)
        print("Age - ", self.age)
        print("Gender - ", self.gender)
        print("Ac No - ",self.ac_no)
        print("")
        print('_'*50)


#Child Class
#Creating Deposit function

class Bank(User):
    def __init__(self,branch,name,age,gender,ac_no):
        super().__init__(branch,name,age,gender,ac_no)
        self.balance = 1000

    def Deposits(self,amount):

        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account Balance has updated: Rs",self.balance)
        print("")

    def Withdrawal(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds, Remaining Balance: Rs",self.balance)
            print("")
        else:
            self.balance = self.balance - self.amount
            print("Account Balance after Withdrawal: Rs",self.balance)
            print("")

    def Passbook(self):
        print('>' * 50)
        print("Bank Of Pune")
        print('>' * 50)
        print("")
        print("")
        print('-' * 50)
        print("Passbook Details")
        print('-'*50)
        self.User_Details()
        print("Account Balance is: Rs",self.balance)
        print('-' * 50)



Customer1 =Bank("Pashan","Shubham",26,"Male",1001)

# Customer1.Deposits(10000)
# Customer1.Deposits(12000)
# Customer1.Withdrawal(6000)
# Customer1.Passbook()






