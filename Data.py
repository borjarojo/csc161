class Data:
    def __init__(self):
        self.data = self.read_AAPL_file()
        self.max = len(self.data) - 1
        self.min = 1

    # Read the file in and return as a list of lists
    def read_AAPL_file(self):
        infile = open("AAPL.csv", "r")       # Open the file

        data = infile.readlines()           # Read file as list of lines
        for i in range(len(data)):          # Run through each line
            data[i] = data[i].split(",")    # And split the data into a list
            data[i][6] = data[i][6].strip() # also trim the endline char off

        for i in range(1, len(data)):
            for j in range(1, 7):
                data[i][j] = float(data[i][j])

        data.reverse()                          # Reverse list
        last = data.pop()                       # Pop column names
        data.insert(0, last)                    # Insert it to the front

        return data

    # Converts the col key to the index in the list of stock data for one day
    def col_convert(self, col):
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

    # Returns the stock price for the given day and type. 
    # Day is between 1 and max
    def getStock(self, dayNumber, stockType):
        return self.data[dayNumber][self.col_convert(stockType)]
