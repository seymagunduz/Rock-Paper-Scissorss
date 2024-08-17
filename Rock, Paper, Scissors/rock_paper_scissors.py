from random import randint

def rock_paper_scissors_SEYMA_GUNDUZ():
    game_number = 0
    game = ["rock", "paper", "scissors", "exit"]
    name = input(f'Hello, please enter your name to start the game:')
    print(f'Welcome to the ---Rock, Paper, Scissors--- game, Dear {name} \nThe Rules: \n - Rock beats Scissors \n - Scissors beats Paper \n - Paper beats Rock \nGame will be over when the score is 2. \nWrite exit for leaving the game.')

    while True:
        user_score = 0
        computer_score = 0
        win_score = 2
        round_number = 0
        game_number += 1
    
        while True:
            computer_choice = game[randint(0, 2)]
            user_choice = input(f'Please, choose rock, paper, scissors or exit: ').lower()
            round_number += 1

            if user_choice == "exit":
                print(f'You have exited the game.')
                return

            if user_choice not in game:
                print('Invalid choice. Please choose rock, paper, scissors or exit.')
                continue

            if computer_choice == user_choice:
                print(f'The game is a draw.\nComputer also chose {computer_choice}. \nGame:{game_number} | Round: {round_number} \n{name}: {user_score} \nComputer: {computer_score}')
        
            elif user_choice == "rock":
                if computer_choice == "paper":
                    computer_score += 1
                    print(f'Sorry :( Computer chose {computer_choice}. You lost this round. \nGame:{game_number} | Round: {round_number} \n{name}: {user_score} \nComputer: {computer_score}')   
                else:
                    user_score += 1
                    print(f'Congratulations! You won this round. Computer chose {computer_choice}. \nGame:{game_number} | Round: {round_number}\n{name}: {user_score} \nComputer: {computer_score}')

            elif user_choice == "paper":
                if computer_choice == "scissors":
                    computer_score += 1
                    print(f'Sorry :( Computer chose {computer_choice}. You lost this round.\nGame:{game_number} | Round: {round_number} \n{name}: {user_score} \nComputer: {computer_score}')   
                else:
                    user_score += 1
                    print(f'Congratulations! You won this round. Computer chose {computer_choice}.\nGame:{game_number} | Round: {round_number} \n{name}: {user_score} \nComputer: {computer_score}')

            elif user_choice == "scissors":
                if computer_choice == "rock":
                    computer_score += 1
                    print(f'Sorry :( Computer chose {computer_choice}. You lost this round.\nGame:{game_number} | Round: {round_number} \n{name}: {user_score} \nComputer: {computer_score}')   
                else:
                    user_score += 1
                    print(f'Congratulations! You won this round. Computer chose {computer_choice}.\nGame:{game_number} | Round: {round_number} \n{name}: {user_score} \nComputer: {computer_score}')
        
            if user_score == win_score:
                print('Congratulations! You won the game!')
                break
        
            if computer_score == win_score:
                print('Sorry, Computer won the game!')
                break


        while True:
            answers = ['yes','no']
            computers_answer = answers[randint(0,1)]

            user_answer = input('Do you wanna play it again? (yes/no)').lower()

            if user_answer not in answers:
                print('Invalid choice. Plesase write yes or no!')
                continue

        
            if user_answer == 'no':
                if computers_answer == 'no':
                    print(f'Computer also does not to play again.Thank you for playing :)')
                    return
                else:
                    print('Oh, computer wants to play it again. Maybe next time..')
                    return

            if user_answer == 'yes':
                if computers_answer == 'no':
                    print(f'Unfortunatelly, computer does not want to play again.')
                    return
                else:
                    print('Computer also wants to play again. Restarting game....')
                    break
       
   
rock_paper_scissors_SEYMA_GUNDUZ()
    