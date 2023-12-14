# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

## Table of Contents
- Description of the project
- Usage instruction
- Installation instructions
- File structure of the project
- License information

## Description of the project
  - This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.
  - The project's goal was to implement knowledge from previous Python lessons to create a hangman program.
  - Main thing I learnt from this project was to use of classes in Python.

## Usage instruction
- Run the milestone5.py file.
- Enter a letter to make a guess.
- You start with 5 lives.
- You lose the game once your lives hit 0.
- You win the game once all letters have been correctly guessed.

## Installation instructions
- Clone the file from github and install python 3.10.7

## File structure of the project
### Milestone 2: Requires basic Python knowledge, such as if-else statements and loops.
- M2 requires to define the list of possible word and also choose a random word from the list. Using random library, a random word can be picked inside a list. This is the code below:
```
#Word list:
["mango","banana","pineapple","strawberry","apple"]

def __init__(self, word_list, num_lives = None):
        self.word_list = word_list
        self.num_lives = 5 
        self.word = random.choice(word_list)
```
The random word is saved in the variable "self.word"

### Milestone 3: Checks if the guessed character is in the word.
- M3 requires to check if the guessed letters is in the randomly chosen word. This was achieved inside the check_guess method which takes in self.guess variable that contains the user's letter.
- A simple if statement checks if the self.word variable contains the user's letter
```
 if self.guess in self.word:
            print (f"Good guess! {self.guess} is in the word")
else:

            print (f"Sorry, {self.guess} is not in the word")
```

### Milestone 4: Use Object Oriented Programming paradigm to develop a complete Hangman game.

### Milestone 5: The complete Hangman Game

