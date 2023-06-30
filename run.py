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
    user_guess_letters = []
    user_guess_words = []
    """
    number of tries the user has to guess the right answer
    """
    chances = 6

    """
    help guide user when they start
    """
    print("Let's start the game!")
    """
    intital state of hangman
    """
    print(draw_hangman(chances))
    """
    initial state of word with all hashtag
    """
    print(cover_word)
    print("\n")

    while not guessed and chances > 0:
        """
        storing guess in guess variable
        making sure it is uppercase
        inside loop 3 conditonal branches based on different user input, 
        whether its guessing a letter, word or typing something other than a letter or word of the correct length
        """
        user_guess = input("Type in a letter or a word...let's see if you get it right!: ").upper()
       
        """
        guess has a length of one and contains only valid alphabet characters
        """
        if len(user_guess) == 1 and user_guess.valid_character():
            if user_guess in user_guess_letters:
                print("Unfortunately, you've already guessed this letter", user_guess)

                """
                user guesses letter not in the word and their number of tries goes down by 1
                """
                elif user_guess in user_guess_letters:
                    print(user_guess, "is not in the word!")
                    chances -= 1
                    user_guess_letters.append(user_guess)

                
                else:
                    print("Well done," user_guess_letters, "is in the word!")
                    user_guess_letters.append(guess)
                    word_as_list = list(cover_word)


        """
        length of guess = length of actual word and contains only letters
        """
        elif len(user_guess) == len(word)and user_guess.valid_character():
        
        """
        else - anything else other than the above
        """
        else:
        print("Not a valid guess!")
  
    """
    print current state of hangman and the word
    """
    print(display_hangman(tries))
    print(cover_word)
    """"
    print new line that spaces out each term
    """"
    print("\n")








def draw_hangman(chances):
    
    each_try = [
        
        """
        +---+
        O   |
            |
            |
       ===''', '''
        """,

        """
        +---+
        O   |
        |   |
            |
       ===''', '''
        """,

        """
        +---+
        O   |
       /|   |
            |
       ===''', '''
        """,

        """
        +---+
        O   |
       /|\ |
        |
       ===''', '''
        """,

        """
        +---+
        O   |
       /|\  |
       /    |
       ===''', '''
        """,

        """
        +---+
        O   |
       /|\  |
       / \  |
        ==='''
        """
    ]


