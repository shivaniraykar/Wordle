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