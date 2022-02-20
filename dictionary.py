import random

def getValidDictionary():
    '''Forms a valid dictionary that just contains 5 letter words'''
    file1 = open('words.txt', 'r')
    words = file1.readlines()
    dictionary = []
    for word in words:
        if len(word.strip()) == 5:
            dictionary.append(word)
    return dictionary

def getRandomWord():
    '''Choose a random word from dictionary'''
    dictionary = getValidDictionary()
    randomWord = random.choice(dictionary).strip()
    #print(randomWord)
    return randomWord

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
