from curses.ascii import isalpha
from dictionary import checkWord, getRandomWord
from ui import getUserInput, wordIsEqualToInput

totalGamePlayedCount:int = 0
gamesWon = 0
distribution = {1: 0, 2:0, 3:0, 4:0, 5:0, 6:0}

def displayStatistic():
    print("------Statistics-------")
    print("Number of games played = ", totalGamePlayedCount)
    winPercentage = (gamesWon/totalGamePlayedCount)*100
    winPercentage = round(winPercentage, 2)
    print("Win Percentage = ", winPercentage,"%")  
    print("-----Game distribution-------") 
    for x in range(1, 7):
        percent = (distribution[x] / totalGamePlayedCount)* 100
        print("Game distribution for ", x, " = ", round(percent, 2))

def main():
    #get a random word from dictionary 
    global totalGamePlayedCount
    global gamesWon
    global distribution
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
                distribution[len(wordList)] = distribution[len(wordList)] + 1
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



