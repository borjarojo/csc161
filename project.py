"""CSC 161 Project

This program:

Reads in stock data from Apple and can look up certain stock values

Borja Rojo
Lab Section TR 2:00-3:15pm
Fall 2016
"""


# Global varianle for Account
# Holds total capital in index 0
# Holds total stocks in index 1
account = [1000, 0]

def test_data(col, day):
    data = read_AAPL_file()
    col_num = col_convert(col)

    return data[day][col_num]

# Read the file in and return as a list of lists
# Columns
def read_AAPL_file():
    infile = open("AAPL.csv","r")       # Open the file

    data = infile.readlines()           # Read file as list of lines
    for i in range(len(data)):          # Run through each line
        data[i] = data[i].split(",")        # And split the data into a list
        data[i][6] = data[i][6].strip()     # also trim the endline char off
    
    for i in range(1, len(data)):
        for j in range(1, 7):
            data[i][j] = float(data[i][j])

    data.reverse()                          # Reverse list
    last = data.pop()                       # Pop column names
    data.insert(0, last)                    # Insert it to the front

    return data

def get_capital():
    return account[0]

def get_stock_count():
    return account[1]

# Converts the col key to the index in the list of stock data for one day
def col_convert(col):
    if col == "open":
        return 1
    elif col == "high":
        return 2
    elif col == "low":
        return 3
    elif col == "close":
        return 4
    elif col == "volume":
        return 5
    elif col == "adj_close":
        return 6

# Arguments are optional. Cleared with professor.
def alg_moving_average(column="close", margin=20, perc_margin=.2):
    # Start by getting an organized copy of the data
    data = read_AAPL_file()

    """The running average will be aquired by holding a continuously 
    updated total average. that average will then be divided by the
    amount of active data points to aquire the average. These parameters
    will be played with to come up with the best strategy.

    """


    capital = account[0]
    stocks = account[1]

    """Trading parameters

    Column: Stock price type used
    Margin: The amount of data being used for the average
    perc_margin: The percentage used to buy and sell stocks
    """
    column = col_convert(column)
    data_margin_total = 0
    perc_diff_var = 0

    # Get the first span of data totaled
    for i in range(1, margin + 1):
        data_margin_total += data[i][column]
    # Now, the total is calculated to the full margin

    #Running average evaluations
    for i in range(margin + 1, len(data)):
        # Calculate precentage difference
        perc_diff_var = perc_diff(data_margin_total / margin, 
                                    data[i][column])

        # Make a decision
        # If diff larger than 20%
        if perc_diff_var >= perc_margin and capital > data[i][column]:
            stocks += 1                 # Buy a stock
            capital -= data[i][column]  # Reduce capital
        # If diff smaller than -20%
        elif perc_diff_var <= (-1 * perc_margin) and stocks > 0:
            stocks -= 1                        # Sell a stock
            capital += data[i][column]         # Return some capital


        # Move average
        data_margin_total -= data[i - margin][column]
        data_margin_total += data[i][column]

    capital += data[len(data) - 1][column] * stocks
    stocks = 0


    return stocks, capital

# Args are optional, cleared with professor.
def alg_mine(column="close"):
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
    
    data = read_AAPL_file()         # Get organized data
    column = col_convert(column)    # Set the column
    capital = account[0]            # Set the capital
    stocks = account[1]             # Set the stocks

    for i in range(1, len(data)):   # For every peice of data
        current_stock_price = data[i][column]
        current_stock_is_vowel = is_vowel(current_stock_price)
        if current_stock_is_vowel == False and capital >= current_stock_price: 
            capital -= data[i][column]
            stocks += 1
        elif current_stock_is_vowel == True:
            capital += data[i][column] * stocks
            stocks = 0

    capital += data[i][column] * stocks
    stocks = 0
    
    return stocks, capital
    
def is_vowel(num):
    modded = (num % 26) // 1 # Mod and floor
    if modded == 0 or modded == 4 or modded == 8 or modded == 14 or modded == 21:
        return True
    return False


def perc_diff(num_one, num_two):
    return (num_one / num_two) - 1

def main():
    alg1_stocks, alg1_balance = alg_moving_average()
    
    alg2_stocks, alg2_balance = alg_mine()

    print("alg_moving_average: Stocks", alg1_stocks," Capital $", alg1_balance)
    #print("alg_mine: Stocks", alg2_stocks, " Capital $", alg2_balance)

if __name__ == '__main__':
    main()
