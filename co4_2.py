class bank:
    __acc_name=""
    __acc_no = ""
    __acc_type = ""
    __acc_balance = 0
    
    def __init__(self,a_name,a_no,a_type,a_balance):
        self.__acc_name = a_name
        self.__acc_no = a_no
        self.__acc_type = a_type
        self.__acc_balance = a_balance
        
    def deposit(self,a_deposit):
        print("Initial balance is  : ",self.__acc_balance)
        print("Deposit is  : ",a_deposit)
        self.__acc_balance += a_deposit
        print("Current balance: ",self.__acc_balance)
        
    def withdraw(self):
        print("Current balance: ",self.__acc_balance)
        self.amount = int(input("Amount to withdraw :"))
        if self.amount > self.__acc_balance:
            print("You don't have enough balance to withdraw !!")
            print("Current balance:",self.__acc_balance)
        else:
            print(self.amount," is withrawed .")
            self.__acc_balance -= self.amount
            print("Current balance:",self.__acc_balance)
            
    def acc_info(self):
       
         print("Account holder name:",self.__acc_name)
         print("Account number:",self.__acc_no)
         print("Account type :",self.__acc_type)
         print("Account Balance:",self.__acc_balance)
       
         
        
def main():
    
    name  = input("Account holder name : ")
    no      = input("Account number:")
    atype  = input("Account type:")
    bal      = int(input("Account initial balance:"))
    holder = bank(name,no,atype,bal)

    while(True):
       
        opt = int(input("1)Deposit \n2)Withdraw \n3)Account info \n0)Exit\nChoose your option :: "))
       
        if opt == 1:
            amount = int(input("Deposit amount:"))
            holder.deposit(amount)
        elif opt == 2:
            holder.withdraw()
        elif opt == 3:
            holder.acc_info()
        elif opt == 0:
            break
        else:
            print("Invalid Option !")
            
if __name__ == "__main__":
    while(True):
        main()
    
