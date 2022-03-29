
InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
   "FirstName": "Cameron",  
   "LastName": "Skelly",  
   "Grade": "10",  
   "Email": "cameronskellyy@gmail.com",  
   "Classes":["AP Chemistry","AP European Culture","AP Calculus","Cermaics", "Spanish 6"]  
              })  

InfoDb.append({  
   "FirstName": "Maile",  
   "LastName": "Weight",  
   "Grade": "10",  
   "Email": "mailew@gmail.com",  
   "Classes":["Physics","World History","Integrated 3B","Cermaics", "Spanish 6"]  
              }) 

InfoDb.append({  
   "FirstName": "Shadi",  
   "LastName": "Lalehzarian",  
   "Grade": "10",  
   "Email": "shadilaleh@gmail.com",  
   "Classes":["AP Chemistry","AP European Culture","Pre Calculus","Photography", "Integrated 3B"]  
              })   

InfoDb.append({  
   "FirstName": "Jack",  
   "LastName": "Smith",  
   "Grade": "12",  
   "Email": "jacksmith@gmail.com",  
   "Classes":["AP Environmental Sciece","Economics","AP Stats","Cermaics", "Offroll"]  
              })   

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Classes: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Classes"]))  # join allows printing a string list with separator
    print()


# for loop iterates on length of InfoDb
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

 # while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

border = "=" * 25

def iteration_tester():
    print (border)
    print("For Loop:")
    for_loop()
    print (border)
    print( "While Loop:")
    while_loop(0)  # requires initial index to start while
    print (border)
    print("Recursive Loop:")
    recursive_loop(0)  # requires initial index to start recursion
    print (border)


if __name__ == "__main__":
    iteration_tester()