from typing import Dict

letterDict = {}

def setLetterDictionary() -> None:
    letterString = "abcdefghijklmnopqrstuvwxyz"
    for letter in letterString:
        letterDict[letter] = [0, 0, 0, 0, 0]

def countFrequency() -> None:
    setLetterDictionary()
    try:
        file1 = open('valid-words.txt', 'r')
    except FileNotFoundError as e:
        print(f"Cannot open file ({e})")
    else:
        words = file1.readlines()
        for word in words:
            for x in range(5):
                letter = word[x]
                list = letterDict.get(letter)
                list[x] = list[x]+1
                letterDict[letter] = list
        for value in letterDict.values():
            for x in range(5):
                value[x] = value[x]/len(words)
        file1.close()

    
def writeInLetterFrequency() -> None:
    countFrequency()
    listToTuple()
    try:
        file1 = open('letterFrequency.csv', 'w')
    except FileNotFoundError as e:
        print(f"Cannot open file ({e})")
    else:
        for key in letterDict:
            tuple = letterDict.get(key)
            file1.write("{},{},{},{},{},{} \n".format(key, tuple[0], tuple[1], tuple[2], tuple[3], tuple[4]))
        file1.close()

def listToTuple() -> None:
    for key in letterDict:
        list = letterDict.get(key)
        letterDict[key] = tuple(list)
    return letterDict


def parseStatisticToTuple() -> Dict:
    tupleDict = {}
    try:
        file1 = open('letterFrequency.csv', 'r')
    except FileNotFoundError as e:
        print(f"Cannot open file ({e})")
    else:
        stats = file1.readlines()
        for stat in stats:
            str:list = stat.strip().split(",")
            tupleDict[str[0]] = tuple(str[1:])
        file1.close()
        return tupleDict


def calculateLikelyhood() -> Dict:
    writeInLetterFrequency()
    tupleDict = parseStatisticToTuple()
    try:
        file1 = open('valid-words.txt', 'r')
    except FileNotFoundError as e:
        print(f"Cannot open file ({e})")
    else:
        words = file1.readlines()
        likelyhoodDict = {}
        for word in words:
            likelyhood = 1
            for x in range(5):
                letter = word[x]
                tuple = tupleDict.get(letter)
                likelyhood = likelyhood * float(tuple[x])
            likelyhoodDict[word.strip()] = likelyhood
        #print(likelyhoodDict)
        file1.close()
        return likelyhoodDict

def writeWordRank() -> None:
    likelyhoodDict = calculateLikelyhood()
    try:
        file1 = open('wordRank.csv', 'w')
    except FileNotFoundError as e:
        print(f"Cannot open file ({e})")
    else:
        sorted_list = sorted(likelyhoodDict.items(), key=lambda x:x[1], reverse=True)
        #print(sorted_list)
        count = 0
        for tupleWord in sorted_list:
            count = count + 1
            file1.write("{},{},{}\n".format(count, tupleWord[0], tupleWord[1]))
        file1.close()
    
