# Wordle 
## Description
This is a simple recreation of Wordle using Python. 
The computer randomly chooses a word as the answer from a 5-letter word dictionary[^1].
The player then inputs 5 letter words to the terminal which are then referenced with the 5-letter word dictionary to see if it is a valid word.
The guess is compared to the answer, and is displayed in the terminal with each letter color coded:
- Black - Letter not in word
- Red - Letter in word, but not in correct spot
- Green - Letter in correct spot
The player continues to guess until they either guess the correct word, in which case they win the game, or run out of guesses (6 tries).
In the case that the player loses, the correct answer is revealed.

[^1]: The 5-letter dicitonary is from [Schmookey](https://gist.github.com/shmookey/b28e342e1b1756c4700f42f17102c2ff)

## Play Loop
The majority of the play loop is within the ```play()``` function. 
The player gets 6 chances to guess the correct answer. 
The terminal asks for the player's guess which is cross-referenced with a 5-letter dictionary. 
In the event that the guess is not in the dicitonary, the guess is not counted and the computer prompts the player for a valid 5-letter word. 
The player's guess is then compared to the answer, and output to the terminal with each letter color coded. 
(All previous guesses are also displayed.)
If the player guesses the answer correctly, the computer tells the player that they won and the program ends.
In the event that the player does not guess the answer correctly within 6 valid guesses, the player loses and displays the correct answer.

```
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
```

## Comparing Guesses with Answers
The ```letters(guess)``` function takes in a valid 5-letter guess from the main ```play()``` function and returns a list of indexes ```in_ans``` which is used to determine the color of each letter.
The indexes correspond to the following:
- 0 if not in answer
- 1 if in answer but not in correct spot (partially correct)
- 2 if in answer and in correct spot (correct)
The function first checks for letters that are in the correct spot, and changes the index of the correct letters in the ```in_ans``` list to ```2```.
For any correct letters, the corresponding letter in the answer is then removed so that it is not counted again in the case that there are multiples of the same letter in the guess.
(the answer is copied to another variable ```ans``` so that the ```global ans``` is not affected).\

The function then checks for guessed letters in the answer, but are not in the correct spot.
To ensure that correct letters are not overwritten, ```in_ans``` is checked to make sure that that index is not already correct in the case that there are two of the same letter in the answer and the player guesses one of them correctly.
Again, for any partially correct letters, the corresponding letter in the answer is then removed so that it is not counted again in the case that there are multiples of the same letter in the guess.

```
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
            # Prevent overwriting if multiple of same letter
            if in_ans[i] != 2:
                in_ans[i] = 1
                index = ans.index(guess[i])
                ans = ans[0:index] + ' ' + ans[index + 1:]
    return in_ans
```
## Acknowledgements
The 5-letter dictionary is from [Schmookey](https://gist.github.com/shmookey/b28e342e1b1756c4700f42f17102c2ff)
