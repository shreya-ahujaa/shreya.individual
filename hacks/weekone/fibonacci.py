
def fibonacci(n): #
           if n <= 1: # if number is 0,1 return number
             return n #return number if these are the inputs
           else:
             return(fibonacci(n-1) + fibonacci(n-2)) #return -1 and -2 of number
           for o in range(n):
              print(fibonacci(o))

def fib_input():
    n = int(input("Enter a number for Fibonacci Sequence:")) 
    try:
      n >= 0 
      if n < 0: 
        print("Sorry, Fibonacci Sequence does not exist for negative numbers!")
    if str(type(n)) != "str":
        print("You have entered something different than an integer. Please enter an integer!") 
    else:
        def fibonacci(n): #
           if n <= 1: 
             return n 
           else:
             return((n-1) + (n-2))
        for o in range(n):
            print(fibonacci(o)) 

    
