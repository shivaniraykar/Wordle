from exceptions import InvalidWord, LengthNotFiveAndAlphabets, SameInput
class UI:
    def __init__(self) -> None:
        self.isWordValid = False
    
    def __str__(self):
        return 'IsWordValid = '+ str(self.isWordValid)

    def getUserInput(self, wordList):
        '''Gets a user input, checks if it's valid and returns it.'''
        try:
            userInput = input("Enter a 5 letter word: ")
            if len(userInput) == 0:
                return 0
            #check if word is valid dictionary word
            isWordValid = self.isWordValidDictionaryWord(userInput)

            #check if word length is 5 and just contains capital alphabets
            if(self.checkLengthNotFiveAndAlphabets(userInput)):
                raise LengthNotFiveAndAlphabets
            elif not isWordValid:
                raise InvalidWord
            elif userInput in wordList:
                #checks if the word was already given as an input
                raise SameInput
            else:
                return userInput
        except LengthNotFiveAndAlphabets:
            self.printWordRestrictionsError()
        except InvalidWord:
            self.printWordNotInDictionaryError()
        except SameInput:
            self.printPriorInputError()
        #finally:
            #displayStatistic()

    def wordIsEqualToInput(self, expectedWord, userInput) -> bool:
        '''Used to check if two words match and returns true or false accordingly'''
        if expectedWord == userInput:
            print("Yay...The words matched!")
            file1 = open("gameplay.log", "a")
            file1.write("Yay...The words matched!")
            file1.close()
            return True
        else:
            return False    

    def isWordValidDictionaryWord(self, userInput) -> bool | None:
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

    def checkLengthNotFiveAndAlphabets(self, userInput) -> bool:
        return (len(userInput) != 5  or not userInput.isalpha())
            
    def printWordRestrictionsError(self) -> None:
        print("Word should just contain alphabets and the length should be 5")

    def printWordNotInDictionaryError(self) -> None:
        print("Word not found in dictionary")

    def printPriorInputError(self) -> None:
        print("You have already given this input. PLease try another word")