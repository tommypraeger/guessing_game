# Guessing Game
This is just a simple guessing game where you try to guess a number from 1 to a chosen maximum number in a limited number of guesses.

The game will prompt you for all inputs. Auto-solve will automatically make optimal guesses for you at every stage. The answer will be an integer from 1 to the maximum number that you chose. For all yes or no questions, respond with "y" or "yes" to answer yes and anything else to answer no.

The number of guesses allowed is equal to log base 2 of the chosen maximum number plus one, so you have to be efficient with your guesses. 
Examples:
- guessing from 1 to 10: log base 2 of 8 = 3.459, so you would have 4 guesses
- guessing from 1 to 1000: log base 2 of 1001 = 9.967, so you would have 10 guesses

## Instructions
### Prerequisites
[Download Python 3](https://www.python.org/downloads) if you haven't already.
### Installation
Run `git clone https://github.com/tommypraeger/guessing_game.git && cd guessing_game` from the command line.
### Usage
Run `python3 guessing_game.py` from the `guessing_game` directory to start the game.
