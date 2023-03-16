# drew.sadler@slu.edu & jordi.carbajal@slu.edu

class ChargeCard:
    def __init__(self, limit, balance=0):
        self._limit = limit
        self._balance = balance
    def getBalance(self):
        return self._balance
    def getLimit(self):
        return self._limit
    def charge(self, amount):
        if amount == 0 or amount < 0:
            raise ValueError
        if not isinstance(amount, int):
            raise TypeError
        if amount + self._balance <= self._limit:
            self._balance += amount
            return True
        else:
             return False            
    def deposit(self, value):
        self._balance -= value
