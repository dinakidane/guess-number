"""
python library import
get random words from the word options variable in the words file
"""

import random
import string
from words import word_options


def select_word():
    chosen_word = random.choice(word_options)
    """
    converting all user input to uppercase to make  it easier for user to clearly read
    """
    return chosen_word.upper()

"""
main area for whole game, random word chosen is covered by #
if user guesses correct letter then it will be revealed and will uncover #
user as a maximum of 6 attempts to get the answer
"""
def game(chosen_word):

    """
    same length as chosen word
    word covered with only hashtags
    """
    cover_word ="#" * len(chosen_word)
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
    print("Welcome to Hangman!")
    print("Let's start the game!")
    """
    intital state of hangman
    """
    print(hangman(chances))
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
        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in user_guess_letters:
                print("You've already guessed this letter", user_guess)

                """
                user guesses letter not in the word and their number of tries goes down by 1
                """
            elif user_guess not in chosen_word:
                print(user_guess, "is not in the word!")
                chances -= 1
                user_guess_letters.append(user_guess)

                
            else:
                print("Well done,", user_guess_letters, "is in the word!")
                user_guess_letters.append(user_guess)
                """
                cover_word from a string to a list so we can index into it, 
                storing this into word_as_list
                """
                word_as_list = list(cover_word)
                indices = [i for i, letter in enumerate(chosen_word) if letter == user_guess]
                for index in indices:
                    word_as_list[index] = user_guess
                cover_word = "".join(word_as_list)
                if "#" not in cover_word: 
                    guessed = True


        """
        length of guess = length of actual word and contains only letters
        """
        if len(user_guess) == len(chosen_word) and user_guess.isalpha():
            if user_guess in user_guess_words:
                print("You've already guessed the word!", user_guess)
            elif user_guess != chosen_word:
                print(user_guess, "is not the word!")
                chances -= 1
                user_guess_words.append(user_guess)
            else:
                guessed = True
                cover_word = chosen_word
        
        
        else:
            print("Not a valid guess!")
        print(hangman(chances))
        print(cover_word)
        print("\n")

    if guessed:
        print("Congratulations! You've guessed the word!")
    else:
        print("Oh no! You didn't guess the word :(. The word was " + chosen_word + ". Maybe next time!")



def hangman(chances):
    
    each_try = [

        #head, body, left arm, right arm, left leg, right leg
        """
        +---+
        O   |
       /|\  |
       / \  |
        ==='''
        """    

        #head, body, left arm, right arm, left leg
        """
        +---+
        O   |
       /|\  |
       /    |
       ===''', '''
        """,

        #head, body, left arm, right arm
        """
        +---+
        O   |
       /|\  |
            |
       ===''', '''
        """,

        #head, body, left arm
        """
        +---+
        O   |
       /|   |
            |
       ===''', '''
        """,

         # head, body
        """
        +---+
        O   |
        |   |
            |
       ===''', '''
        """,

        # head
        """
        +---+
        O   |
            |
            |
       ===''', '''
        """,

        # orignal state, empty
        """
        +---+
            |
            |
            |
        ===    
        """
    ]
    return each_try[chances]


"""
taking user back to the starting area of the game
"""
def main():
    chosen_word = select_word()
    game(chosen_word)
    while input("Would you like to play again? (Y/N)"). upper() == "Y":
        chosen_word = select_word()
        game(chosen_word)

if __name__ == "__main__":
    main()