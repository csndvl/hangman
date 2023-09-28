import random
import string 


word_list = ["mango","banana","pineapple","strawberry","apple"]
word = random.choice(word_list)

guess = input("Please enter a single letter: ")
if len(guess) == 1 and guess not in (string.punctuation) and guess not in ("1","2","3","4","5","6","7","8","9","0"):
    print ("Good Guess")
else:
    print("Oops! That is not a valid input")


print (word)

