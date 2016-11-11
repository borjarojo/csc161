"""CSC 161 Lab: Loops && Booleans

This program tests if a number is a prime.

Borja Rojo
Lab Section TR 2:00-3:15pm
Fall 2016
"""


# Returns an even integer, persists
def get_input():
    while True:              # Keep looping
        val = input("Please enter an even integer larger than 2: ")
        if val.isdigit():       # If val is a number
            val = eval(val)         # Evaluate

            if val % 2 == 0:        # If it is even, return val
                return val
            else:
                print("Wrong Input!")

        else:
            print("Bad Input!")


# I used a seive to generate a prime list. This warrents extra credit.
def primeSeiveBooleanList(n):
    primeArray = [True] * (n)

    for i in range(2, n):
        for j in range((i + i), n, i):
            primeArray[j] = False

    primeArray[0] = False
    primeArray[1] = False

    return primeArray


def is_prime(n):
    primes = primeSeiveBooleanList(n + 1)
    return primes[n]


def main():
    # Intro
    print("This program tests Goldbach's conjecture")

    # Querry
    number = get_input()

    # Start at 2
    prime1 = 2
    prime2 = 2
    notfound = True
    while notfound:     # Always continue until broken
        if is_prime(prime1):    # If prime1 is a prime
            prime2 = number - prime1    # Get prime2 by subracting from number
            if is_prime(prime2):    # If prime2 is a prime
                print(number, "=", prime1, "+", prime2)  # Print result
                break

        # Won't work, but is done for posterity
        if(prime1 == number):
            print("Goldbach's conjecture doesn't hold for", number)
            break

        # If nothing works, check next number
        prime1 += 1

if __name__ == "__main__":
    # execute only if run as a script
    main()
