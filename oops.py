from Bank_account import *

Dave = BankAccount(1000 , "Dave")
Sara = BankAccount(2000 , "sara")

Dave.get_balance()
Sara.get_balance()

Sara.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(10000 , Sara)
Dave.transfer(100 , Sara)

Jim = InterestRewardsAcct(1000, "Jim")

Jim.get_balance()

Jim.deposit(100)

Jim.transfer(100 , Dave)

Blaze = SavingAcct(1000 , "Blaze")

Blaze.get_balance()

Blaze.deposit(100)

Blaze.transfer(1000 , Sara)
Blaze.transfer(1000 , Sara)