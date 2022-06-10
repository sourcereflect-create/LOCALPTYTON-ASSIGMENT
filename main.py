
import random

#R:Rock | P:Paper | S:Scissors, entered repititions to improve randomness
options_dict = {"R":"Rock", "P":"Paper", "S":"Scissors"}
options = ["R", "P", "S", "P", "R", "S"] 


def run_game():
    computer = random.choice(options)
    #print(f'computer {computer}')
    
    user = input("Enter your selection from this list [R,P,S]:")
    
    while user not in options:
        if user not in options:
            print ('invalid input detected')
        user = input("Enter your selection from this list [R,P,S]:")
    
    print(f'Player ({options_dict[user]}) | CPU ({options_dict[computer]})')
    
    if user == computer:
        print("It's a Tie!")
        run_game()
    else:
        index_dict = {0: "User", 1: "CPU"}
        pair = [user,computer]
        if "R" in pair and "S" in pair:
            print(f"Winner = {index_dict[pair.index('R')]}")
        elif "P" in pair and "R" in pair:
            print(f"Winner = {index_dict[pair.index('P')]}")
        elif "S" in pair and "P" in pair:
            print(f"Winner = {index_dict[pair.index('S')]}")
        
        print('Game Over!')
        replay = input("Want a Replay? Y / N :")
        
        if replay == "Y" or replay == "y":
            run_game()
        else:
            print("Game terminated")

        


run_game()

  




