def findFactors(number):
    print("Factors of a Given Number {0} are:".format(number))
    for value in range(1, number + 1):
        if number % value == 0:
            print("{0}".format(value), end=" ")
    print()

def factors():
    num = int(input("Enter any Number to find its factors: "))
    findFactors(num)

factors_of = factors() 
def test_data():
  factors(20)
  factors(factors(256))
  
def factor_input():
  while True:
      n = int(input("Choose a Number to Factorize:"))
      try:
            n = int(n)
            if n <= 0:
                raise ValueError
            print("Factors of {0} is: ".format(n))
            print(factors_of(n))
      except ValueError:
            print(f'Positive integer number is expected, got "{n}" Try again.')

