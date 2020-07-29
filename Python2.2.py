import random
comp_choice=random.randrange(1,4)
user_comp= input("Enter your choice:Rock, Paper, Scissors ")

while True:
    if user_comp =="Rock":
        if comp_choice==2:
            print ("computer won, computer picked paper")
            break
        elif comp_choice==3:
            print ("user won, computer picked scissors")
            break
        else:
            print("Draw, please play again")
    elif user_comp =="Paper":
        if comp_choice==1:
            print ("user won, computer picked rock")
            break
        elif comp_choice==3:
            print ("computer won, computer picked scissors")
            break
        else:
            print("Draw, please play again")
    else:
        if comp_choice==1:
            print ("computer won, computer picked rock")
            break
        elif comp_choice==2:
            print ("user won, computer picked paper")
            break
        else:
            print("Draw, please play again")