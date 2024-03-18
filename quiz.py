from questions import questions, python_answers

def intro(player):
    print(' -----------------------------------------------------------------------------------------')
    print(f'                         Welcome to The Python Quiz {player}!                              ')
    print("   There are a total of 10 questions, you can skip a question anytime by typing 'SKIP'    ")
    print(' -----------------------------------------------------------------------------------------')

def play_game():
    index = 1
    score = 0 
    player_answers = []

    for question, options in questions.items():
        print()
        print(f'{index}.{question}')
        for option in sorted(options):
            print('  ', option)
        player_answer = input('Choose the correct answer A, B, C or D: ').upper()
        player_answers.append(player_answer)
        print('-' * 40)

        if player_answer.upper() == 'SKIP':
            pass
        elif player_answer == python_answers[index - 1]: 
            print('CORRECT!\n')
            score += 1
        else:
            print('INCORRECT! Correct answer:', python_answers[index - 1])
            print()
        index += 1
    
    return score
    
def display_score(player, score):
    final_score = int((score / len(questions)) * 100)

    print('\n--- Quiz Results ---')
    print(f'Player: {player}')
    print(f'Score: {score} of {len(questions)} or {final_score}%')


def play_again():
    choice=input("\nDo You Want To Play Again? (Y/N):  ").upper()
    
    if choice == 'Y':
        return True
    else:
        print('Thank you for playing! :)')
        return False


player = input('Write your name: ').capitalize()
intro(player)


while True:
    score = play_game()
    display_score(player , score)
    if not play_again():
        break

