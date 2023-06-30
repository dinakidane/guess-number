"""
python library import
get random words from the word options variable in the words file
"""

import random
from words import word_options


def valid_word():
    word = random.choice(word_options)
    """
    converting all user input to uppercase to make  it easier for user to clearly read
    """
    return word.upper()

def play(word):

    """
    words completition is same length as chosen word
    initially contain only underscores
    """
    word_completion ="_" * len(word)
    """
    guessed intiliaised to false
    """
    guessed = False
    """
    holds letters and words that user guesses
    """
    guessed_letters = []
    guessed_words = []
    """
    number of tries, corrsponding number of bodyparts left to be drawn on the hangmn before the user loses
    head, body, both arms and both legs
    """
    tries 6


