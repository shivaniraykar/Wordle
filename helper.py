from email.policy import default
from linkedlist import LinkedList
def split(word):
    return list(word)

def getWordRank(word):
    file1 = open('wordRank.csv', 'r')
    lines = file1.readlines()
    for line in lines:
        list = line.split(",")
        if(list[1] == word):
            return list[0]
    return

def getPossibleWords(goodLetter, badLetter, wordDict):
    #goodLetter = input("Enter the good letters(that are included in the words) : ")
    #badLetter = input("Enter the bad letters(that are not included in the words) : ")
        

    if(goodLetter or badLetter):
        valid_words_file = open('valid-words.txt','r')
        words = valid_words_file.readlines()
        result = []
        l1 = LinkedList()
        l2 = LinkedList()
        word_dict = {}
        if badLetter:
            badLetter_list = split(badLetter)
            for word in words:
                word = word.strip()
                has_no_badLetters = any([char in word for char in badLetter_list])
                if(has_no_badLetters == False):
                    result.append(word)
        if goodLetter:
            # letter1 = input("Enter the correct letter at position 1 : ")
            # letter2 = input("Enter the correct letter at position 2 : ")
            # letter3 = input("Enter the correct letter at position 3 : ")
            # letter4 = input("Enter the correct letter at position 4 : ")
            # letter5 = input("Enter the correct letter at position 5 : ")
            letter1 = wordDict.get(0, None)
            letter2 = wordDict.get(1, None)
            letter3 = wordDict.get(2, None)
            letter4 = wordDict.get(3, None)
            letter5 = wordDict.get(4, None)
            goodLetter_list = split(goodLetter)

            

            if len(result) > 0:
                words = result
            
            for word in words:
                word = word.strip()
                has_all_goodLetters = all([char in word for char in goodLetter_list])
                if has_all_goodLetters == True:
                    l2.insert(word)
                    if(letter1):
                        if(word[0] != letter1.strip()):
                            continue
                    if(letter2):
                        if(word[1] != letter2.strip()):
                            continue
                    if(letter3):
                        if(word[2] != letter3.strip()):
                            continue
                    if(letter4):
                        if(word[3] != letter4.strip()):
                            continue
                    if(letter5):
                        if(word[4] != letter5.strip()):
                            continue
                    l1.insert(word)
            
            if l1.head:
                current = l1.head
            else:
                current = l2.head

        if l1.head or l2.head:
            while(current):
                word_dict[current.data] = int(getWordRank(current.data.strip()))
                current = current.next
        else:
            for word in result:
                word_dict[word] = int(getWordRank(word.strip()))

        sorted_list = dict(sorted(word_dict.items(), key=lambda x:x[1], reverse=True))
        keyList = [key for key in sorted_list]
        return keyList[0]
            
    else:
        file1 = open('wordRank.csv', 'r')
        lines = file1.readlines()
        result = []
        for line in lines:
            list = line.split(",")
            result.append(list[1])
        return result[0]
        

# def main():
#     x = getPossibleWords()
#     if(len(x) > 0):
#         print(*x, sep = "\n")
#     else:
#         print('No such combination exists')

# if __name__ == '__main__': 
#     main()



        


