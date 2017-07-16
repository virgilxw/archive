# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    output = []
    counter = 0
    
    if lettersGuessed == []:
        return False
    
    for letter in secretWord:
        for i in lettersGuessed:
            if letter == i:
                counter = 0
                output += i
                break
            elif counter == len(lettersGuessed)-1:
                return False
            else:
                counter += 1
    
    return True
    
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    output = ""
    counter = 0 
    for letter in secretWord:
       for i in lettersGuessed:
            if letter == i:
                counter = 0
                output += i
                output += ' '
                break
            
            elif counter == len(lettersGuessed)-1:
                output += '_ '
                counter = 0
            else:
                counter += 1
                
    return (output)

def getAvailableLetters(lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    alphabet = string.ascii_lowercase
    
    for element in lettersGuessed:
        alphabet = alphabet.replace(element, '')
                
    return alphabet
    
def main(secretWord, lettersGuessed, numberOfGuesses):
    '''
    Recursive function to test secretWord
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    '''
    
    print ("-------------")
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print ("Congratulations, you won!")
        return
    elif numberOfGuesses == 0:
        print ("Sorry, you ran out of guesses. The word was "+ secretWord + '.')
        return
    
    print ("You have", numberOfGuesses, "guesses left.")
    print ("Available letters:", getAvailableLetters(lettersGuessed))
    
    guess = input ("Please guess a letter:")
    guess = guess.lower()
    getGuessedWord(secretWord, lettersGuessed)
    
    
    flag = False
    while flag == False:
        if guess.isalpha() == False or len(guess) > 1:
            guess = input ("Previous guess invalid. Try again:")
        elif guess in lettersGuessed:
            print ("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            main(secretWord, lettersGuessed, numberOfGuesses)
            guess = input()
        else:
            flag = True            
            
    lettersGuessed.append(guess)
    
    
    if guess in secretWord:
        print ("Good guess:", getGuessedWord(secretWord, lettersGuessed))
    else:
        print ("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        numberOfGuesses -= 1
        
    main(secretWord, lettersGuessed, numberOfGuesses)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    lettersGuessed =[]
    numberOfGuesses = 8
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is", len(secretWord),"letters long.")
    main(secretWord, lettersGuessed, numberOfGuesses)
    





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
