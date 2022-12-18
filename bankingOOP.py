# Instance variables : name , amount , address
# Class variables : Bank_name , ROI_On_FD
# Instance methods : CreateAccount() , account_info()
# Class methods : displaybankInformation()
# Static method :
class Bank_Account:

    bank_name = "HDFC bank pbt limited"
    ROI_On_FD = 6.7

    def __init__(self):
        self.name = ""
        self.amount = 0
        self.address = ""
        self.accountNo = 0

    def CreateAccount(self):
        self.name = input("Enter your Name : ")
        self.amount = int(input("Enter your initial amount : "))
        self.address = input("Enter your address : ")
        self.accountNo = int(input("Enter your account number : "))

    def account_info(self):
        print(f"------Account Information of {self.name} ------")
        print("Name : ",self.name)
        print("Amount : ",self.amount)
        print("Address : ",self.address)
        print("Account Number : ",self.accountNo)

    @classmethod
    def displayBankInformation(cls):
        print("Welcoming to Banking Console")
        print("Name of our bank is : ",cls.bank_name)
        print("Rate of interest we offer on fixed deposite is : ",cls.ROI_On_FD)

    @staticmethod
    def displayKYCInfo():
        print("Please consider below KYC Information")
        print("According to rules of government of india you have to submit below documents")
        print("1.Clear and recent passport size photo")
        print("2.Photo of aadhar card")
        print("3.Photo of PAN card")

    def Deposite(self):
        value = int(input(f"Enter the money to be Deposites in {self.name} Account : "))
        self.amount = self.amount + value

    def Withdraw(self):
        value = int(input(f"Enter the money to be Withdraw from {self.name} Account : "))
        self.amount = self.amount - value

def main():
    Bank_Account.displayKYCInfo()
    print()

    print("Name of bank : ",Bank_Account.bank_name)
    print("Name of interest on Fixed deposit : ",Bank_Account.ROI_On_FD)
    print()

    Bank_Account.displayBankInformation()
    print()

    user1 = Bank_Account()
    print()
    user2 = Bank_Account()
    print()

    print("Enter the information of User1")
    user1.CreateAccount()
    print()

    print("Enter the information of User2 ")
    user2.CreateAccount()
    print()

    user1.account_info()
    print()
    user2.account_info()
    print()

    user1.Deposite()
    print()
    user2.Deposite()
    print()

    print(f"Amount of {user1.name} after Deposite : ",user1.amount)
    print()
    print(f"Amount of {user2.name} after Deposite : ", user2.amount)
    print()

    user1.Withdraw()
    print()
    user2.Withdraw()
    print(f"Amount of {user1.name} after Withdraw : ",user1.amount)
    print()
    print(f"Amount of {user2.name} after Withdraw : ", user2.amount)
if __name__ == "__main__":
    main()