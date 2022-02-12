from curses.ascii import isalpha
from dictionary import getRandomWord
from ui import getUserInput, wordIsEqualToInput

totalGamePlayedCount:int = 0
gamesWon = 0


def countLetters(expectedWord):
    '''counts how many times a letter is present in a given word'''
    letter_count: dict = {}
    for i in range(len(expectedWord)):
        letter_count[expectedWord[i]] = letter_count.get(expectedWord[i], 0) + 1
    return letter_count

def checkWord(userInput, expectedWord):
    '''Used to comapre the userInput and expectedWord and returns the result'''
    result = []
    letter_count: dict = countLetters(expectedWord)    

    for i in range(len(expectedWord)):
        if userInput[i] == expectedWord[i]:
            result.append(" ")
            letter_count[userInput[i]] -= 1
        else:
            result.append('"')

    for i in range(len(expectedWord)):
        if userInput[i] != expectedWord[i]:
            if userInput[i] in letter_count:
                if letter_count[userInput[i]] > 0:
                    result[i] = '`'
                    letter_count[userInput[i]] -= 1
    return result

def displayStatistic():
    print("------Statistics-------")
    print("Number of games played = ", totalGamePlayedCount)
    winPercentage = (gamesWon/totalGamePlayedCount)*100
    winPercentage = round(winPercentage, 2)
    print("Win Percentage = ", winPercentage,"%")   

def main():
    #get a random word from dictionary 
    global totalGamePlayedCount
    global gamesWon
    expectedWord = getRandomWord()
    wordList = []

    #Until a exit condition is given or program exits take a user input and check if valid
    while len(wordList) < 6:
        userInput = getUserInput(wordList)
        if userInput == 0:
            break
        if userInput is None:
            continue
        else:
            wordList.append(userInput)
            isUserInputEqualToWord = wordIsEqualToInput(expectedWord, userInput)
            if isUserInputEqualToWord:
                gamesWon = gamesWon + 1
                totalGamePlayedCount = totalGamePlayedCount + 1
                displayStatistic()
                print("-----New Challenge Begin!-----")
                main()
            ans = checkWord(userInput, expectedWord)
            print(''.join(ans))
    else:
        print("You have reached the maximum attempts!")
        totalGamePlayedCount = totalGamePlayedCount + 1
        displayStatistic()
        print("\n-----New Challenge Begin!-----")
        main()

main()



