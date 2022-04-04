from dictionary import Dictionary
from statistics import writeWordRank
from helper import getPossibleWords
from ui import UI

class Wordle:
    def __init__(self, dictObj, ui_obj) -> None:
        self.totalGamePlayedCount = 0
        self.gamesWon = 0
        self.distribution = {1: 0, 2:0, 3:0, 4:0, 5:0, 6:0}
        self.selectedWordList = []
        self.dict = dictObj
        self.ui_obj = ui_obj
    
    def __str__(self):
        return 'Total games played = '+ str(self.totalGamePlayedCount)+ ' and total games won = '+ str(self.gamesWon)

    def calculateWinPercentage(self) -> float:
        winPercentage = (self.gamesWon/self.totalGamePlayedCount)*100
        winPercentage = round(winPercentage, 2)
        return winPercentage
        
    def displayStatistic(self) -> None:
        print("------Statistics-------")
        print("Number of games played = ", self.totalGamePlayedCount)
        winPercentage = self.calculateWinPercentage()
        print("Win Percentage = ", winPercentage,"%")  
        print("-----Game distribution-------") 
        for x in range(1, 7):
            percent = (self.distribution[x] / self.totalGamePlayedCount)* 100
            print("Game distribution for ", x, " = ", round(percent, 2))
        self.displayStatisticsInFile()

    def displayStatisticsInFile(self) -> None:
        try:
            file1 = open("gameplay.log", "a")
        except FileNotFoundError as e:
            print(f"Cannot open file gameplay.log ({e})")
        else:
            file1.write("\n------Statistics-------\n")
            file1.write("Number of games played = {} \n".format(self.totalGamePlayedCount))
            winPercentage = self.calculateWinPercentage()
            file1.write("Win Percentage = {}% \n".format(winPercentage))
            file1.write("-----Game distribution-------\n") 
            for x in range(1, 7):
                percent = (self.distribution[x] / self.totalGamePlayedCount)* 100
                file1.write("Game distribution for {} = {}\n".format(x, round(percent, 2)))
            file1.close()

    def play(self) -> None:
        #get a random word from dictionary 
        ##global gamesWon
        #global distribution
        expectedWord = self.dict.getRandomWord(self.selectedWordList)
        wordList = []

        #Until a exit condition is given or program exits take a user input and check if valid
        while len(wordList) < 6:
            userInput = self.ui_obj.getUserInput(wordList)
            if userInput == 0:
                self.totalGamePlayedCount = self.totalGamePlayedCount + 1
                self.displayStatisticsInFile()
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
                isUserInputEqualToWord = self.ui_obj.wordIsEqualToInput(expectedWord, userInput)
                if isUserInputEqualToWord:
                    self.gamesWon = self.gamesWon + 1
                    self.distribution[len(wordList)] = self.distribution[len(wordList)] + 1
                    self.totalGamePlayedCount = self.totalGamePlayedCount + 1
                    self.displayStatistic()
                    print("-----New Challenge Begin!-----")
                    self.play()
                ans = self.dict.checkWord(userInput, expectedWord)
                print(''.join(ans))
        else:
            print("You have reached the maximum attempts!")
            self.totalGamePlayedCount = self.totalGamePlayedCount + 1
            self.displayStatistic()
            print("\n-----New Challenge Begin!-----")
            self.play()

    def playWithHelper(self) -> None:
        expectedWord = self.dict.getRandomWord(self.selectedWordList)
        wordList = []
        userInput = "sales"
        while len(wordList) < 6:
            print(f"User input {len(wordList)} : {userInput}\n")
            self.totalGamePlayedCount = self.totalGamePlayedCount + 1
            #self.displayStatisticsInFile()
            wordList.append(userInput)
            try:
                file1 = open("gameplay.log", "a")
            except FileNotFoundError as e:
                print(f"Cannot open file gameplay.log ({e})")
            else:
                file1.write("The user input for try {} : {} \n".format(len(wordList), userInput))
                file1.close()
            isUserInputEqualToWord = self.ui_obj.wordIsEqualToInput(expectedWord, userInput)
            if isUserInputEqualToWord:
                self.gamesWon = self.gamesWon + 1
                self.distribution[len(wordList)] = self.distribution[len(wordList)] + 1
                self.totalGamePlayedCount = self.totalGamePlayedCount + 1
                break
                #self.displayStatistic()
            ans = self.dict.checkWord(userInput, expectedWord)
            print(''.join(ans))
            goodLetterList = self.dict.goodLettersList
            badLetterList = self.dict.badLettersList
            word_dict = self.dict.word_dict
            userInput = getPossibleWords(goodLetterList, badLetterList, word_dict)
            print(userInput)

def main():
    dict = Dictionary()
    ui_obj = UI()
    Game = Wordle(dict, ui_obj)
    dict.getValidDictionary()
    writeWordRank()
    #Game.play()
    Game.playWithHelper()
    #print(Game)
    #print(dict)
    #print(ui_obj)

if __name__ == '__main__': 
    main()



