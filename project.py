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

def alg_moving_average():
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
    column = col_convert("close")
    margin = 15     # This is the span of the average
    data_margin_total = 0
    perc_margin = .05
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

def perc_diff(num_one, num_two):
    return (num_one / num_two) - 1

def main():
    alg1_stocks, alg1_balance = alg_moving_average()

    print(alg1_stocks, alg1_balance)

main()