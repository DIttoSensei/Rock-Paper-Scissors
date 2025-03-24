# A simple Rock Paper Scissors Game 

import random


def main ():
    player_input = input("ROCK PAPER SCISSORS? : " + "\nYou: ").capitalize()
 

    # Validate user input
    if player_input not in ['Rock', 'Paper', 'Scissors']:
        print("Invalid input. Please enter Rock, Paper or Scissors.")
        return
    
    ai_choice = computer_choice()
    result = process(player_input , ai_choice)
    print (result)


def computer_choice():
    # Define the choices
    choices = ['Rock', 'Paper', 'Scissors']
    ai_choice = random.choice(choices)
    print("AI: " + ai_choice)
    return ai_choice


    
def process (player_input, ai_choice):
    if ai_choice == player_input:
        return 'It a tie!'
    elif (ai_choice == 'Rock' and player_input == 'Scissors') or \
          (ai_choice == 'Scissors' and player_input == 'Paper') or \
          (ai_choice == 'Paper' and player_input == 'Rock'):
        return 'AI wins!'
    else:
        return 'Player wins!'
        



if __name__ == '__main__':
    main()