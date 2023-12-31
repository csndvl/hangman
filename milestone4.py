import random

class Hangman():

    def __init__(self, word_list, num_lives = None):
        self.word_list = word_list
        self.num_lives = 5 
        self.word = random.choice(word_list)
        self.num_letters = 26
        self.list_of_guesses = []

        self.empty_word = []
        for letters  in self.word:
            letters = "_"
            self.empty_word.append(letters)

        self.filled_word = []
        for letters in self.word:
            self.filled_word.append(letters)

        print(f"You have {self.num_lives} lives")
        print(f"{self.empty_word}\n")

        Hangman.ask_for_input(self)
        # self.word_guessed = filled_word

    def check_guess(self, guess):
        self.guess = guess.lower()
        self.num_letters -= 1
        if self.guess in self.word:
            print (f"Good guess! {self.guess} is in the word")
            for letter in self.filled_word:
                if letter == self.guess:
                    index = self.filled_word.index(letter)
                    self.filled_word[index] = 0
                    self.empty_word[index] = self.guess
            print (f"{self.empty_word}\n")
            Hangman.ask_for_input(self)
        else:
            self.num_lives -= 1
            print (f"Sorry, {self.guess} is not in the word")
            print (f"You have {self.num_lives} lives left")
            print (f"{self.empty_word}\n")
            if self.num_lives == 0:
                print ("GAME OVER!!!!")
            else:
                Hangman.ask_for_input(self)
                
    def ask_for_input(self):
        self.guess = input("Please enter a letter: ")
        while True:
            if self.guess.isalpha() == True:
                if self.guess in self.list_of_guesses:
                    print("You already tried that letter\n")
                    Hangman.ask_for_input(self)
                else:
                    self.list_of_guesses.append(self.guess)
                    Hangman.check_guess(self, self.guess)
            else:
                print ("Invalid letter\n")
                Hangman.ask_for_input(self)


word_list = ["mango","banana","pineapple","strawberry","apple"]
player1 = Hangman(word_list)

