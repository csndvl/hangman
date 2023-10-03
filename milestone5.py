import random


class Hangman():
    '''Creates a hangman class.'''

    def __init__(self, word_list, num_lives = None):
        self.word_list = word_list
        self.num_lives = 5 
        self.word = random.choice(word_list)
        self.num_letters = len(self.word)
        self.list_of_guesses = []

        self.empty_word = ["_" for _ in self.word] #Turns the word to be guesses into a blank letter  
        self.filled_word = list(self.word) #Puts the word to be guessed into a list; letter by letter

        print(f"You have {self.num_lives} lives")
        print ("Please guess the word")
        print(f"{self.empty_word}\n")
        Hangman.ask_for_input(self)

    def check_guess(self):
        '''Checks the letter guessed by the user if it's in the word or not.'''
        if self.guess in self.word:
            print (f"Good guess! {self.guess} is in the word")
            for letter in self.filled_word:
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
            else:
                Hangman.ask_for_input(self)
        else:
            self.num_lives -= 1
            print (f"Sorry, {self.guess} is not in the word")
            print (f"You have {self.num_lives} lives left")
            print (f"{self.empty_word}\n")
            if self.num_lives == 0:
                print ("GAME OVER!!!!")
                exit()
            else:
                Hangman.ask_for_input(self)
                
    def ask_for_input(self):
        '''Asks the user to guess a letter.'''
        self.guess = input("Please enter a letter: ")
        self.guess = self.guess.lower()
        while True:
            if self.guess.isalpha() == True and len(self.guess) == 1: #This line checks if the input is a singular string.
                if self.guess in self.list_of_guesses: #Checks whether the guess has been tried already.
                    print("You already tried that letter\n")
                    Hangman.ask_for_input(self)
                else:
                    self.list_of_guesses.append(self.guess) #Adds the new letter to the list of guesses.
                    Hangman.check_guess(self)
            else:
                print ("Invalid letter\n")
                Hangman.ask_for_input(self)


def play_game(word_list):
    '''Starts the game.'''
    num_lives = 5
    game1 = Hangman(word_list, num_lives)   

play_game(["mango","banana","pineapple","strawberry","apple"])