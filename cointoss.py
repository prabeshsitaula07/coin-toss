import random

print("Lets have a coin toss.")
call = ["head", "tail"]
my_call = (input("What is your call? Head or Tail : ")).lower()
appears = random.choice(call)

def check():
    if my_call == "head":
        print("You choose head.")
    elif my_call == "tail":
        print("You choose tail.")

check()
print(f"It appears {appears}")
def toss():
    if (my_call == "head" and appears == "tail") or (my_call == "tail" and appears == "head"):
        print("opponent won the toss.")
    elif (my_call == "tail" and appears == "tail") or (my_call == "head" and appears == "head"):
        print("you won the toss.")
    else:
        
        print(f"Your call {my_call} is invalid.\nTry again")
        
toss()