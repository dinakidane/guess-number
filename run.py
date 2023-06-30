"""
python library import
get random words from the word options variable in the words file
"""

import random
from words import word_options


def select_word():
    word = random.choice(word_options)
    """
    converting all user input to uppercase to make  it easier for user to clearly read
    """
    return word.upper()

"""
main area for whole game, random word chosen is covered by #
if user guesses correct letter then it will be revealed and will uncover #
user as a maximum of 6 attempts to get the answer
"""
def game(word):

    """
    same length as chosen word
    word covered with only hashtags
    """
    cover_word ="#" * len(word)
    """
    guessed starts with being false
    """
    guessed = False
    """
    holds letters and words that user guesses
    """
    user_input_letters = []
    user_input_words = []
    """
    number of tries the user has to guess the right answer
    """
    chances = 6

def draw_hangman(chances):
    
    each_try = [
        +---+
        O   |
            |
            |
       ===''', '''
        +---+
        O   |
        |   |
            |
       ===''', '''
        +---+
        O   |
       /|   |
            |
       ===''', '''
        +---+
        O   |
       /|\ |
        |
       ===''', '''
        +---+
        O   |
       /|\  |
       /    |
       ===''', '''
        +---+
        O   |
       /|\  |
       / \  |
        ==='''
    ]


