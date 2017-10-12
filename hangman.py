# 
# Hangman game
# -----------------------------------
#

import random
import string

#Enter absolute path of the wordlist file
WORDLIST_FILENAME = "R:\Hangman\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

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
    for l in secretWord:
        if l not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ""
    for l in secretWord:
        if l not in lettersGuessed:
            guessedWord += " _"
        else:
            guessedWord += l
    return guessedWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = ""
    for l in string.ascii_lowercase:
        if l not in lettersGuessed:
            availableLetters += " "+l
    return availableLetters
    
    
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
    print "Welcome to the game, Hangman!"
    length = len(secretWord)
    print "I am thinking of a word that is " + str(length) + " letters long."
    print "---------------"
    guessesLeft = 8
    lettersGuessed = []
    availableLetters = getAvailableLetters(lettersGuessed)
    while guessesLeft > 0 or getGuessedWord(secretWord, lettersGuessed) == secretWord:
         print "You have " + str(guessesLeft) + " guesses left."
         print "Available letters: " + availableLetters
         inp = raw_input("Please guess a letter: ")
         inp = inp.lower()
         lettersGuessed += inp
         if inp not in availableLetters:
             print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
             print "---------------"
             continue
         if inp in secretWord:
             if getGuessedWord(secretWord, lettersGuessed) == secretWord:
                 print "Good guess: " + secretWord
                 break;
             print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)                  
         else:
             print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
             guessesLeft -= 1
         availableLetters = getAvailableLetters(lettersGuessed)
         print "---------------"
    if guessesLeft ==0:
         print "Sorry, you ran out of guesses. The word was " + secretWord + "."
    else:
        print "---------------"
        print "Congratulations, you won!"


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
