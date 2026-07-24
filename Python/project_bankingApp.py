class BankingApp:
    Total_Amount = 0
    # count = 0
    def withdrawl(self,Amount ):
        if self.Total_Amount== 0 :
            with open("transactin.txt", 'a') as file:
                file.write(f"\n Transaction completed. your Total Amount is {self.Total_Amount}")
            print("Not enough money. Try again")
        else:
            with open("transactin.txt", 'a') as file:
                file.write(f"\n Transaction completed. your Total Amount is {self.Total_Amount}")
            self.Total_Amount = self.Total_Amount - Amount
            print(f"Sucessfull withdrawl of {Amount} , Money left in Account {self.Total_Amount}")

    def diposit(self,Amount):
        if Amount<= 0:
            with open("transactin.txt", 'a') as file:
                file.write(f"\n Transaction completed. your Total Amount is {self.Total_Amount} ")
            print(f"Very low Amount , cannot be deposited ")
        else:
            with open("transactin.txt", 'a') as file:
                file.write(f"\n Transaction completed. your Total Amount is {self.Total_Amount}")
            self.Total_Amount= self.Total_Amount + Amount
            print(f"Deposit successfull. Your current Balance is {self.Total_Amount}")
    def trasaction(self):
        with open("transactin.txt", "r") as file:
            last_line = file.readlines()[-1]
            print(last_line)


Bank = BankingApp()

while True:
    print("""
        Press 1 : To withdrawl
        Press 2 : To Diposit
        Press 3 : To see last Trasaction Details.
        Press 4 : Exit Application
    """)
    try:
        to_do = int(input("What you want to do? "))
        if to_do == 1 :
           Amount= int(input("Enter the amount you want to withdraw : "))
           Bank.withdrawl(Amount) 
        elif to_do == 2 :
            Amount= int(input("Enter the amount you want to Deposit : "))
            Bank.diposit(Amount)
        elif to_do == 3:
            Bank.trasaction()
        elif  to_do == 4 :
            print("Thank You")
            break
        else:
            print("Invalid Input")

    except Exception:
        print("Invalid Input.")

    