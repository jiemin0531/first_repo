class Account:
    def __init__(self):
        self.balance = 0

    def withdrawal(self,money):
        if self.balance<money:
            print("餘額不足")
        else:
            self.balance = self.balance - money
    
    def top_up(self,money):
        self.balance = self.balance + money

    def show_balance(self):
        print(self.balance)