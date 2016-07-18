from random import *
user_Input = []
get_Input = raw_input("You ready for the M.A.S.H tho?")
user_Input.append(get_Input)
print(user_Input)

def main():
    what = [" You will live", "u will live", "You will live", "You will live", "You will live",
        "U will live"]
    are = ["in a mansion, earning 10Mill Weekly", "on the streets, a broke bum", "in a loft with friends, earning minimum wage", "in the white house", "in their parents basement", "in a Hotel, as a salesperson"]
    those = ["married to JLO", "with 7 Children", "best friends with J.Cole", " ", "as a successful actor, earning 1 mill a movie", "as a Talk show host"]
    user_Input = []
    get_Input = raw_input("Trying to do M.A.S.H , with out your name, whats your name slime")
    user_Input.append(get_Input)
    user_Input = []
    get_Input = raw_input("Where do you wanna live bro?")
    user_Input.append(are)
    user_Input = []
    get_Input = raw_input("with whom?")
    user_Input.append(those)
    print(what[randrange(len(what))]+" "+ (are[randrange(len(are))])+" "+ (those[randrange(
          len(those))]))
        
main()

##  from random import is to make it draw randomly but not in order
## user  input and so on from that part is questioning and append means to place
z