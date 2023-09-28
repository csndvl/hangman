word = "apple"

def ask_for_input():
    guess = input("Please enter a letter: ")
    while True:
        if guess.isalpha() == True:
                check_guess(guess)
        else:
            print ("Invalid letter")
            ask_for_input()

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print (f"Good guess! {guess} is in the word")
        ask_for_input()
    else:
        print (f"Sorry, {guess} is not in the word")
        ask_for_input()




ask_for_input()
