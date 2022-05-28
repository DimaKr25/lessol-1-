class Client:
    def __init__(self, name, balance, creditBalance, passport):
        self.__name = name
        self.__balanceOwnFunds = balance
        self.__balanceCreditFunds = creditBalance
        self.__passport
    def addOwnFunds(self, money):
        self.balanceOwnFunds =+ money
    def addCreditFunds(self, money):
        self.balanceCreditFunds =+ money
    def printPrivateDate(self):
        print(self.__name, self.__balanceOwnFunds, self.__balanceCreditFunds, self.__passport)

account = Client("Bobib", 1000, 300,)