from random import *
user_Input = []
get_Input = raw_input("You ready for the M.A.S.H tho?")
user_Input.append(get_Input)
print(user_Input)

def main():
    user_Input = []
    get_Input = raw_input("Trying to do M.A.S.H without your name? come on what your name?")
    user_Input.append(get_Input)
##     print(user_Input)
##     what =  print(user_Input)  - Cant put a function inside a variable
##     what = [" YG will live", "Ashim will live", "Oscar will live", "John will live", "Sam will live",
##         "Dan will live"]
    are = ["in a mansion, earning 10Mill Weekly", "on the streets, a broke bum", "in a loft with friends, earning minimum wage", "in the white house", "in their parents basement", "in a Hotel, as a salesperson"]
    those = ["married to JLO", "with 7 Children", "best friends with J.Cole", " ", "as a successful actor, earning 1 mill a movie", "as a Talk show host"]
##     user_Input = []
##     get_Input = raw_input("Trying to do M.A.S.H , with out your name, whats your name slime")
##     user_Input.append(what)
    user_Input = []
    get_Input = raw_input("Where do you wanna live bro?")
    are.append(user_Input)
    user_Input = []
    get_Input = raw_input("with whom?")
    those.append(user_Input)
    print(user_Input+" "+ (are[randrange(len(are))])+" "+ (those[randrange(
          len(those))]))
        
##         {
##          print(what[randrange(len(what))]+" "+ (are[randrange(len(are))])+" "+ (those[randrange(
##           len(those))]))
##         }
##     print(what[randrange(len(what))]+" "+ (are[randrange(len(are))])+" "+ (those[randrange(
##           len(those))]))
##         
main()

##  from random import is to make it draw randomly but not in order
## user  input and so on from that part is questioning and append means to place
## in the list which is [insert here]
## def main is the function and all those under and indented will be included in the
## function. by including user input and so on in each list it will ask the user
## questions and will insert those in the list but will still be picked randomly.