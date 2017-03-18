class Account:
    def __init__(self):
        self.capital = 1000
        self.stocks = 0

    def get_capital(self):
        return self.capital

    def get_stocks(self):
        return self.stocks

    def set_stocks(self, num):
        self.stocks = num

    def add_capital(self, num):
        self.capital += num

    def add_stocks(self, num):
        self.stocks += num

    def sub_capital(self, num):
        self.capital -= num

    def sub_stocks(self, num):
        self.stocks -= num

    def __repr__(self):
        return "Capital: ${0:.2f} Stocks: {1}".format(self.capital, self.stocks)
