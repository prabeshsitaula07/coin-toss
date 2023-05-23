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
    else:
        print("Your call is invalid.")

check()
def toss():
    if my_call == "head" and appears == "tail":
        print("you lost the toss.")
    else:
        print("you won the toss.")
        
print(f"It appears {appears}")
toss()