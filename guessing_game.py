import math
import random
import time
from collections import defaultdict


def guessing_game(num_numbers=None, autosolve=None):
    '''Runs the game'''

    if autosolve is None:
        autosolve = get_yes_no_answer('Do you want to turn auto-solve on? (y/N) ')
    if num_numbers is None:
        num_numbers = choose_num_numbers()

    again = True
    while again:
        max_guesses = math.ceil(math.log2(num_numbers + 1))
        plural = 'es' if max_guesses != 1 else ''

        print(f'You have {max_guesses} guess{plural}!')

        target = random.randint(1, num_numbers)
        guess = 0
        guesses = 0
        min_num = 1
        max_num = num_numbers
        try:
            while guess != target and guesses < max_guesses:
                if not autosolve:
                    guess = int(input(f'Guess {guesses + 1}: '))
                    guess_num(guess, target)
                else:
                    time.sleep(0.1)
                    guess = (min_num + max_num) // 2
                    print(f'Guess {guesses + 1}: {guess}')
                    guess_num(guess, target)
                    if guess > target:
                        max_num = guess - 1
                    else:
                        min_num = guess + 1
                guesses += 1

            if guesses == max_guesses and guess != target:
                again = ask_play_again(False, guesses, num_numbers, autosolve)
            else:
                again = ask_play_again(True, guesses, num_numbers, autosolve)
            break
        except ValueError:
            print('Please enter a number')


def guess_num(guess, target):
    '''Prints clue given a guess and the target number'''

    if guess > target:
        print('Guess lower!')
    elif guess < target:
        print('Guess higher!')


def ask_play_again(won, guesses, num_numbers, autosolve):
    '''Asks whether the use wants to play again

    Asks about settings changes and starts a new game if yes
    '''

    if won:
        print(f'You win! You used {guesses} guesses.')
        again = get_yes_no_answer('Play again? (y/N) ')
    else:
        again = get_yes_no_answer('You lost! Play again? (y/N) ')
    if again:
        autosolve = ask_change_autosolve(autosolve)
        num_numbers = ask_change_num_numbers(num_numbers)
        guessing_game(num_numbers, autosolve)
    else:
        print('Bye!')
    return again


def ask_change_num_numbers(num_numbers):
    '''Asks user if they want to change number of numbers to guess from'''

    change_num_numbers = get_yes_no_answer(
        'Do you want to change how many numbers to guess from? (y/N) '
    )
    if change_num_numbers:
        return None
    else:
        return num_numbers


def ask_change_autosolve(autosolve):
    '''Asks user if they want to change whether auto-solve is on'''

    change_autosolve = get_yes_no_answer(
        'Do you want to change whether auto-solve is on? (y/N) '
    )
    if change_autosolve:
        return not autosolve
    else:
        return autosolve


def choose_num_numbers():
    '''Asks user how many numbers they want to guess from'''

    while True:
        try:
            num_numbers = int(input('Choose how many numbers to guess from: '))
            if num_numbers > 0:
                break
            else:
                print('Please enter a positive integer')
        except ValueError:
            print('Please enter a number')
    return num_numbers


def get_yes_no_answer(question):
    '''Gets a yes or no answers from the user given a question
    
    Defaults to no
    '''

    response_dict = defaultdict(lambda: False, {'y': True, 'yes': True})
    return response_dict[input(question).lower()]


# Starts the game when the script is run
guessing_game()
