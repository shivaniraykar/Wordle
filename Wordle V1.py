# declare a hidden word to SONAR
# declare a list named wordList to store the userinputs
# while length of wordList is less than 7
#   Input the word
#   convert the word to uppercase
#   if user enters prior word
#       print message "You have already given this input. PLease try another word"
#   else if word length is not 5 or word contains any number or symbol or small letters
#       print message "Word should just contain alphabets and the length should be 5"
#   else
#       add the word into the wordList
#       if the userInput and the hidden word match
#           print message "Yay...The words matched!"
#           exit the program
#       else 
#           compare characters in the userInput and the hidden word
#               if two characters match 
#                   print message "Character (alphabet) is at correct place"
#               else if character is present in hidden word
#                   print message "Character (alphabet) is present in the word"
#               else
#                   print message "Character (alphabet) is not present in the word"
# end while loop
# exit the program notify user that he has reached the maximum attempts!


from curses.ascii import isalpha
import sys


word = "SONAR"
wordList = []
    
def compare(word1, word2):
    for x, y in zip(word1, word2):
        if x==y:
            print("Character ", y ,"is at correct place")
        elif word.find(y) != -1 :
            print("Character ", y , "is present in the word")
        else:
            print("Character ", y , "is not present in the word")
        
while len(wordList) < 6:
    userInput = input("Enter a 5 letter word: ")
    #userInput = userInput.upper()
    if userInput in wordList:
        print("You have already given this input. PLease try another word")
        continue
    elif len(userInput) != 5  or not userInput.isalpha() or not userInput.isupper():
        print("Word should just contain capital alphabets and the length should be 5")
        continue
    else:
        wordList.append(userInput)
        if word == userInput:
            print("Yay...The words matched!")
            sys.exit()
        compare(word, userInput)



sys.exit("You have reached the maximum attempts!")

