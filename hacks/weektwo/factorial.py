import random

class factorial:
    def __init__(number):
        number.factorial = [1, 1]
      
    def __call__(number, n):
        if n < len(number.factorial):
            return number.factorial[n]
        else:
            # Compute the requested Factorial number
            factorial_number = n* number(n - 1) 
            number.factorial.append(factorial_number)
        return number.factorial[n]


def factorial_tester():
    # Make a factorial object
    while True:
        factorial_of = factorial()
        n = input("Enter the number of terms: ")
        try:
            n = int(n)
            # Validate the value of n
            if n <=0:
                raise ValueError
            # Factorial term corresponding to n
            print(f"The {n} Term of Factorial Sequence is: ", factorial_of(n - 1))
            # Produces a list of factorial values, one factorial result for each step in range
            print(f"Factorial Sequence of {n} Terms is: ", [factorial_of(o) for o in range(n)])
            break
        except ValueError:
            print(f'Positive integer number expected, got "{n}" Please try again with positve!')


if __name__ == "__main__":
   factorial_tester(random.randint(0,100))
