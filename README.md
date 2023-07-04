# Hangman

Hangman is a straightforward game that requires a player to guess a specific word that has been randomly selected. 
 The players need to guess letters from the alphabet and have 6 attempts to try and get it right.
Each answer they get wrong leads to the process of the stickman getting hanged and the aim is to stop
this from happening.

[My Project](https://hangman-pyth-eee58bb863df.herokuapp.com/)

![Responsive Image](./images/responsiveness.png)

## Features

### Existing features

- Intro to the game

    - The user is welcomed into the game. 
    - This is then followed by a small section to instruct the user how to play. 
    - They are then met with a message that prompts them to start playing the game. 

    ![Game intro](./images/game-intro.png)

- Main game area

    - The hashtags represent the random word that has been selected 
    - The empty drawing of the where the hangman would be suggests the intial state of the hangman 
    because the user hasn't inserted a wrong letter just yet

    ![Start game](./images/start-game.png)

    - The user will get a specific response letting them know if the letter the chose is not in the selected word
    - This will also be followed by the hangman being drawn
    - If the letter that the user has typed in isn't part of the alphabet, there will be no response
    - This will indicate that the user has typed an invalid character. It won't take away the number of attempts
    
    ![Wrong answer](./images/wrong.png)

    - The user will also get a response if the letter they input was in the word they're looking for

    ![Right letter](./images/reply-game.png)

    - The user will be congratulated if they end up guessing the word
    - They will also be asked if they want to play again

    ![Congratulations](./images/right.png)

    - The user will also have the letters that they have chosen on display
    - This prevents them from typing the same letter again and again
    - This is also followed by the number of attempts they have left so the user is aware

    ![Attempts](./images/attempt.png)

### Features left to implement

## Testing

## Deployment

## Bugs

## Credits

## Acknowledgements