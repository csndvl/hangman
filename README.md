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
- M4 objective is to create a class for the hangman game so different instances can be played.
- This was created using a simple OOP
- A snipet of the code where OOP is implemented
```
class Hangman():
    '''Creates a hangman class.'''

def __init__(self, word_list, num_lives = None):
  pass

def check_guess(self):
        '''Checks the letter guessed by the user if it's in the word or not.'''
  pass

def ask_for_input(self):
        '''Asks the user to guess a letter.'''
  pass

def play_game(word_list):
    '''Starts the game.'''
    num_lives = 5
    game1 = Hangman(word_list, num_lives)   

play_game(["mango","banana","pineapple","strawberry","apple"])
```

### Milestone 5: The complete Hangman Game
- M5 goal was to add the game logic; losing life when the user guessed a wrong letter and winning condition.
- This was met by adding a self.num_lives variable which stores the user's remaining lives and once it hits 0, the game is over. In contrast, when the self.num_letters variable, which contains how many more letters needs to be guess equal to 0, the user wins.
```
#Winning Condition
if letter == self.guess:
                    self.num_letters -= 1
                    index = self.filled_word.index(letter)
                    self.filled_word[index] = 0
                    self.empty_word[index] = self.guess
                    #Would like to know a better way of doing this section
            print (f"{self.empty_word}\n")
            if self.num_letters == 0:
                print (" YOU WIN!!!!")
                exit()

#Losing Condition
else:
            self.num_lives -= 1
            print (f"Sorry, {self.guess} is not in the word")
            print (f"You have {self.num_lives} lives left")
            print (f"{self.empty_word}\n")
            if self.num_lives == 0:
                print ("GAME OVER!!!!")
                exit()
```
