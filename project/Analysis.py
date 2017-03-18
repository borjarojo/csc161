class Analysis:
    def __init__(self, data, account):
        self.data = data
        self.account = account
    # Arguments are optional. Cleared with professor.
    def alg_moving_average(self, column="close", margin=20, perc_margin=.2):
        """The running average will be aquired by holding a continuously
        updated total average. that average will then be divided by the
        amount of active data points to aquire the average. These parameters
        will be played with to come up with the best strategy.

        """

        """Trading parameters

        Column: Stock price type used
        Margin: The amount of data being used for the average
        perc_margin: The percentage used to buy and sell stocks
        """
        data_margin_total = 0
        perc_diff_var = 0

        # Get the first span of data totaled
        for i in range(1, margin + 1):
            data_margin_total += self.data.getStock(i, column)
        # Now, the total is calculated to the full margin

        # Running average evaluations
        for i in range(margin + 1, len(self.data.data)):
            # Calculate precentage difference
            perc_diff_var = self.perc_diff(data_margin_total / margin, self.data.getStock(i, column))

            # Make a decision
            # If diff larger than 20%
            if perc_diff_var >= perc_margin and self.account.get_capital() > self.data.getStock(i, column):
                self.account.add_stocks(1)                 # Buy a stock
                self.account.sub_capital(self.data.getStock(i, column))  # Reduce capital
            # If diff smaller than -20%
            elif perc_diff_var <= (-1 * perc_margin) and self.account.get_stocks() > 0:
                self.account.sub_stocks(1)                       # Sell a stock
                self.account.add_capital(self.data.getStock(i, column))         # Return some capital

            # Move average
            data_margin_total -= self.data.getStock(i - margin, column)
            data_margin_total += self.data.getStock(i, column)

        self.account.add_capital(self.data.getStock(len(self.data.data) - 1, column) * self.account.get_stocks())
        self.account.set_stocks(0)


    # Args are optional, cleared with professor.
    def alg_mine(self, column="close"):
        """This is a version of the stock trading algorithm that is determined
        by a custom parameter. The idea is that the current stock price being
        looked at will be compared to the alphabet. If it is a vowel, sell,
        otherwise buy.

        This will be done by modding the stock price by 26 and then checking to
        see if the number returned matches with a vowel.

        A = 0 | E = 4 | I = 8 | O = 14 | U = 21

        This will be evaluated using another function that returns True of False
        depending on the result: is_vowel

        The data will be run through each day and determine the decision.
        Specifically, it will buy a stock for each consinent and sell all the
        stocks for each vowel..

        """

        for i in range(1, len(self.data.data)):   # For every peice of data
            current_stock_price = self.data.getStock(i, column)
            current_stock_is_vowel = self.is_vowel(current_stock_price)
            if current_stock_is_vowel is False and self.account.get_capital() >= current_stock_price:
                self.account.add_stocks(1)                 # Buy a stock
                self.account.sub_capital(self.data.getStock(i, column))  # Reduce capital
            elif current_stock_is_vowel is True:
                self.account.add_capital(self.data.getStock(i, column))   
                self.account.set_stocks(0)

        self.account.add_capital(self.data.getStock(i, column) * self.account.get_stocks())
        self.account.set_stocks(0)


    def is_vowel(self, num):
        modded = (num % 26) // 1  # Mod and floor
        if (modded == 0 or
            modded == 4 or
            modded == 8 or
            modded == 14 or
                modded == 21):
            return True

        return False


    def perc_diff(self, num_one, num_two):
        return (num_one / num_two) - 1

    def __repr__(self):
        return self.account.__repr__()

