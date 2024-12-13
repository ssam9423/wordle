# Wordle Recreation - Samantha Song - started 2024.12.13

# Recreate a wordle
# Using 5-letter word dictionary from shmookey on github
# Randomly choose word as answer
# Take in user's guess
# Check to see if user's guess is a valid word (in dictionary)
# Compare user's guess to answer
# Output user's guess with colors indicating:
#   Black - Letter not in word
#   Red - Letter in word, but not in correct spot
#   Green - letter in correct spot
# Continue until user guesses word correct or user has made 6 guesses


# Import Packages
import pandas as pd
import random
from colored import fg

# Import 5-letter dicitonary & Initialize variables
dict = pd.read_csv("https://gist.githubusercontent.com/shmookey/b28e342e1b1756c4700f42f17102c2ff/raw/ed4c33a168027aa1e448c579c8383fe20a3a6225/WORDS", header=None)
num_words = dict.shape[0]
random.seed()
answer = dict.iloc[random.randint(0, num_words) , 0]
guesses = []
colors = ['black', 'red', 'green']


# Check to see if each letter is in answer
# Returns an list of integers corresponding to each letter in guess
#   0 if not in answer
#   1 if in answer but not in correct spot
#   2 if in answer and in correct spot
def letters(guess):
    # Checks to see if each letter is in answer
    in_ans = [0, 0, 0, 0, 0]
    ans = answer
    # Checks or 2
    for i in range(5):
        if guess[i] == ans[i]:
            in_ans[i] = 2
            ans = ans[0:i] + ' ' + ans[i + 1:]
    # Checks for 1
    for i in range(5):
        if guess[i] in ans:
            in_ans[i] = 1
            index = ans.index(guess[i])
            ans = ans[0:index] + ' ' + ans[index + 1:]
    return in_ans


def play():
    while len(guesses) < 6:
        try:
            guess = input("Type in your guess: ")
            if dict.isin([guess]).any().any():
                color_ind = letters(guess)
                guesses.append([guess, color_ind])
                print(fg('black'), end='')
                print("\nYour Guesses so far: ")
                for word in range(len(guesses)):
                    for letter in range(5):
                        print(fg(colors[guesses[word][1][letter]]), end='')
                        print(guesses[word][0][letter], end='')
                    print(fg('black'), '')
                print()
            else:
                raise ValueError
            if guess.lower() == answer:
                print(fg('green'), end='')
                print("You won!")
                break
        except ValueError:
            print("Please input a valid guess: ")
    print("The answer was: " + answer)


play()

