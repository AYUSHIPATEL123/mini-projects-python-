from mainclass import Main_Account,InterestBonusAccount,SavingsAccount

naruto=Main_Account("Naruto","naruto1@gmail.com",1000)
saske=Main_Account("Saske","saske1@gmail.com",1000)
naruto.get_balance()
naruto.deposit(100)
naruto.withdrow(100)
naruto.transfer(10000,saske)
kakashi=InterestBonusAccount("Kakashi","kaakshi1@gmail.com",2000)
kakashi.deposit(100)
Hinata=SavingsAccount("Hinata","hinata1@gmail.com",1000)
Hinata.transfer(100,naruto)