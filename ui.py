from dictionary import getValidDictionary
from exceptions import InvalidWord, LengthNotFiveAndAlphabets, SameInput
#from wordle import displayStatistic


def getUserInput(wordList):
    '''Gets a user input, checks if it's valid and returns it.'''
    try:
        userInput = input("Enter a 5 letter word: ")
        if len(userInput) == 0:
            return 0
        #check if word is valid dictionary word
        isWordValid = isWordValidDictionaryWord(userInput)

        #check if word length is 5 and just contains capital alphabets
        if(checkLengthNotFiveAndAlphabets(userInput)):
            raise LengthNotFiveAndAlphabets
        elif not isWordValid:
            raise InvalidWord
        elif userInput in wordList:
            #checks if the word was already given as an input
            raise SameInput
        else:
            return userInput
    except LengthNotFiveAndAlphabets:
        printWordRestrictionsError()
    except InvalidWord:
        printWordNotInDictionaryError()
    except SameInput:
        printPriorInputError()
    #finally:
        #displayStatistic()

def wordIsEqualToInput(expectedWord, userInput):
    '''Used to check if two words match and returns true or false accordingly'''
    if expectedWord == userInput:
        print("Yay...The words matched!")
        return True
    else:
        return False    

def isWordValidDictionaryWord(userInput):
    '''Checks if userInput is a valid dictionary word and return true or false accordingly'''
    try:
        wordList = open('valid-words.txt').read().split()
    except FileNotFoundError as e:
        print(f"Cannot open file valid-words.txt ({e})")
    else:
        for word in wordList:
            if word.strip() == userInput:
                return True
        return False

def checkLengthNotFiveAndAlphabets(userInput):
    return (len(userInput) != 5  or not userInput.isalpha())
        
def printWordRestrictionsError():
    print("Word should just contain alphabets and the length should be 5")

def printWordNotInDictionaryError():
    print("Word not found in dictionary")

def printPriorInputError():
    print("You have already given this input. PLease try another word")