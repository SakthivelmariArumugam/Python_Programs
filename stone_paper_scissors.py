import random
def get_choices():
    player_choice=input("Enter a choice(rock,paper,scissors:")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices
def check_win(player,computer):
    print(f"You chose {player},computer chose {computer}")
    if player==computer:
        return "it's a tie!"
    elif player=="rock":
        if computer=="scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers the rock! you loss!"
    elif player=="paper":
        if computer=="Rock":
            return "paper cover the Rock! You win!"
        else:
            return "scissors cut the paper! you loss!"
    elif player=="scissors":
        if computer=="rock":
            return "Rock smashes scissors! You loss!"
        else:
            return "scissors cut the paper! you win!"
            
    
choices=get_choices()
p_choice=choices["player"]
c_choice=choices["computer"]
result=check_win(p_choice,c_choice)
print(result)


          
