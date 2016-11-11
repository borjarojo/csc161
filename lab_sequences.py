"""CSC 161 Lab: Sequences

The programs reads a file with data and displays it nicely.

Borja Rojo
Lab Section TR 2:00-3:15
Fall 2016
"""


def main():
    # Introduction
    print("This program read in financial information from a file\n"
          "and prints it neatly to the user's screen.\n")

    # Read file
    fileName = input("Please enter the filename of the financial data: ")
    print("")
    readFile = open(fileName, "r")
    lineList = readFile.readlines()
    readFile.close()  # File close

    # Print first three lines
    print("Length of the term (years): {0}".format(lineList[0].split()[1]))
    print("The initial principal is: "
          "${0:0.2f}".format(float(lineList[1].split()[1])))
    print("Annual percentage rate is: "
          "{0:0.3f}%".format(float(lineList[2].split()[1])))

    # Print the rest of the lines
    print("\nYear\tValue\n"
          "------------------")
    for i in range(3, len(lineList)):
        print("|{0:>3}\t${1:>0.2f}|".format(str(i), float(lineList[i])))
    print("------------------")

main()
