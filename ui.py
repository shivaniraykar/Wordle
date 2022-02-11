from dictionary import getValidDictionary


def getUserInput(wordList):
    '''Gets a user input, checks if it's valid and returns it.'''
    userInput = input("Enter a 5 letter word: ")
    if len(userInput) == 0:
        return 0
    #check if word is valid dictionary word
    isWordValid = isWordValidDictionaryWord(userInput)

    #check if word length is 5 and just contains capital alphabets
    if(len(userInput) != 5  or not userInput.isalpha()):
        print("Word should just contain alphabets and the length should be 5")
        return
    elif not isWordValid:
        print("Word not found in dictionary")
        return
    elif userInput in wordList:
        #checks if the word was already given as an input
        print("You have already given this input. PLease try another word")
        return
    else:
        return userInput

def wordIsEqualToInput(expectedWord, userInput):
    '''Used to check if two words match and returns true or false accordingly'''
    if expectedWord == userInput:
        print("Yay...The words matched!")
        return True
    else:
        return False    

def isWordValidDictionaryWord(userInput):
    '''Checks if userInput is a valid dictionary word and return true or false accordingly'''
    wordList = getValidDictionary()
    for word in wordList:
        if word.strip() == userInput:
            return True
    return False