import json , random , string
from pathlib import path



class Bank:
    
    database = 'data.json'
    data = []
    
    with open(database) as f:
        data = json.load(f.read())
    def create_account(self):
        pass




user = Bank()
while(True):
    print("""1.Create Account
2.Deposit
3.Withdraw
4.Details
5.Update details
6.Delete
7.Exit""")
    
    choice : int = int(input("Enter Your choice: "))
    
    match(choice):
        case 1 : user.create_account()
        
    