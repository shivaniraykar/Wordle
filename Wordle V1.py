from curses.ascii import isalpha
from dictionary import checkWord, getRandomWord, getValidDictionary
from ui import getUserInput, wordIsEqualToInput

totalGamePlayedCount:int = 0
gamesWon = 0
distribution = {1: 0, 2:0, 3:0, 4:0, 5:0, 6:0}

def calculateWinPercentage():
    winPercentage = (gamesWon/totalGamePlayedCount)*100
    winPercentage = round(winPercentage, 2)
    return winPercentage

def displayStatistic():
    print("------Statistics-------")
    print("Number of games played = ", totalGamePlayedCount)
    winPercentage = calculateWinPercentage()
    print("Win Percentage = ", winPercentage,"%")  
    print("-----Game distribution-------") 
    for x in range(1, 7):
        percent = (distribution[x] / totalGamePlayedCount)* 100
        print("Game distribution for ", x, " = ", round(percent, 2))
    displayStatisticsInFile()

def displayStatisticsInFile():
    try:
        file1 = open("gameplay.log", "a")
    except FileNotFoundError as e:
        print(f"Cannot open file gameplay.log ({e})")
    else:
        file1.write("\n------Statistics-------\n")
        file1.write("Number of games played = {} \n".format(totalGamePlayedCount))
        winPercentage = calculateWinPercentage()
        file1.write("Win Percentage = {}% \n".format(winPercentage))
        file1.write("-----Game distribution-------\n") 
        for x in range(1, 7):
            percent = (distribution[x] / totalGamePlayedCount)* 100
            file1.write("Game distribution for {} = {}\n".format(x, round(percent, 2)))
        file1.close()

def play():
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
            totalGamePlayedCount = totalGamePlayedCount + 1
            displayStatisticsInFile()
            break
        if userInput is None:
            continue
        else:
            wordList.append(userInput)
            try:
                file1 = open("gameplay.log", "a")
            except FileNotFoundError as e:
                print(f"Cannot open file gameplay.log ({e})")
            else:
                file1.write("The user input for try {} : {} \n".format(len(wordList), userInput))
                file1.close()
            isUserInputEqualToWord = wordIsEqualToInput(expectedWord, userInput)
            if isUserInputEqualToWord:
                gamesWon = gamesWon + 1
                distribution[len(wordList)] = distribution[len(wordList)] + 1
                totalGamePlayedCount = totalGamePlayedCount + 1
                displayStatistic()
                print("-----New Challenge Begin!-----")
                play()
            ans = checkWord(userInput, expectedWord)
            print(''.join(ans))
    else:
        print("You have reached the maximum attempts!")
        totalGamePlayedCount = totalGamePlayedCount + 1
        displayStatistic()
        print("\n-----New Challenge Begin!-----")
        play()

def main():
    getValidDictionary()
    play()

main()



