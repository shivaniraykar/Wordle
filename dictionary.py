import random

class Dictionary:
    def __init__(self) -> None:
        self.validWordsCount = 0
        self.goodLettersList = ""
        self.badLettersList = ""
        self.word_dict = {}
    
    def __str__(self):
        return 'Total valid words = '+ str(self.validWordsCount)
   
    def getValidDictionary(self) -> None:
        '''Forms a valid dictionary that just contains 5 letter words'''
        try:
            try:
                file1 = open('words.txt', 'r')
                valid_words_file = open('valid-words.txt','w')
            except FileNotFoundError as e:
                print(f"Cannot open file ({e})")
            else:
                words = file1.readlines()
                for word in words:
                    if len(word.strip()) == 5:
                        valid_words_file.write("{} \n".format(word.strip()))
                file1.close()
                valid_words_file.close()
        except Exception as e:
            print(f"{e}")
    
    def getRandomWord(self, selectedWordList) -> str | None:
        '''Choose a random word from dictionary'''
        try:
            file1 = open("gameplay.log", "a")
            file2 = open('valid-words.txt')
        except FileNotFoundError as e:
            print(f"Cannot open file ({e})")
        else:
            randomWord = ""
            self.validWordsCount = len(file2.readlines())
            if(len(file2.readlines()) == len(selectedWordList)):
                selectedWordList = []
            while True:
                randomWord = random.choice(open('valid-words.txt').read().split()).strip()
                if(randomWord not in selectedWordList):
                    selectedWordList.append(randomWord)
                    break
            file1.write("\n------------New Game-----------\n")
            file1.write("The selected word is : {} \n".format(randomWord))
            file1.close()
            #print(' '.join(selectedWordList))
            print(randomWord)
            return randomWord

    def countLetters(self, expectedWord) -> dict | None:
        try:
            '''counts how many times a letter is present in a given word'''
            letter_count: dict = {}
            for i in range(len(expectedWord)):
                letter_count[expectedWord[i]] = letter_count.get(expectedWord[i], 0) + 1
            return letter_count
        except Exception as e:
            print(f"{e}")

    def checkWord(self, userInput, expectedWord):
        '''Used to compare the userInput and expectedWord and returns the result'''
        try:
            result = []
            letter_count: dict = self.countLetters(expectedWord)    
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
                            
            #changes for helper function
            for i in range(5):
                x = userInput[i] not in self.goodLettersList
                if result[i] == ' ' and x:
                    self.goodLettersList = self.goodLettersList + userInput[i]
                    self.word_dict[i] = userInput[i]
                elif result[i] == '`' and x:
                    self.goodLettersList = self.goodLettersList + userInput[i]

            for i in range(5):
                if result[i] == '"' and userInput[i] not in self.goodLettersList:
                    self.badLettersList = self.badLettersList + userInput[i]

            return result
        except Exception as e:
            print(f"{e}")

