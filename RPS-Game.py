import random
def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ")
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer": computer_choice}

    '''
    Another way to assign computer choice 
    
    computer_choice = ['rock', 'paper', 'scissors']
    choice = {"player": player_choice, "computer": computer_choice[randome.randrange(0, 3)]}
    '''
    return choices

def check_win(player, computer):
    print(f"Your chose {player} and computer chose {computer}.") # This is f string to use variable in sentence
    if player == computer:
        return "It's a tie."
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! Youu lose!"
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cuts paper! You lose!"
        else:
            return "Paper covers rock! You Win!"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors! You lose!"
        else:
            return "Scissors cuts paper! You win!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)