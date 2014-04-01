#word greater then 7 guesses
# milling
# whizzer
# buffs
# cocky
# home
# lore
# losing
# migs
# fisher
# yang
# uric
# gooders
# lined
# viz
# hp
# piqued
# huger
# mint
# forming
# mulls
# gout
# mating
# zarfs
# mines
# gun
# cuppy
# waited
# durn
# bourn
# richer


#here is my general stragety
# look at every single word in the possibilites
# find all words that are possible
    # for example
    # if I currently know (Jacob) **c**
    # it would get all words of length 5
    # with a c in the 3 position
    # then it would count all the letters in this new list
        # which ever letter had the highest count it would choose
        # as the next best guess
    # will repeat this process until the word is solved

from time import time
from interface import Interface
from wordDictionary import WordDict
from random import randrange

def getHighestLetterCount(wordList, noLetters):
    # no letters represent letters that have already been guessed
    # example ["daniel","goldie","eek"] e should be returned most used character
    letterCount = {}
    for word in wordList:
        for char in word:
            if char not in letterCount.keys():
                letterCount[char] = 1
            else:
                letterCount[char] += 1

    maxLetter = ""
    maxValue = 0
    for numLetter, numValue in letterCount.items():
        if numValue > maxValue and numLetter not in noLetters:
            maxValue = numValue
            maxLetter = numLetter
    return maxLetter

def doesWordMatch(word, knownWord):
    # example **c** Jacob would return true
    # **c** potato would return false
    for i in range(len(knownWord)):
        if knownWord[i] != "*":
            if knownWord[i] != word[i]:
                return False
    return True

def updatePossibleList(currentList, guessedLetters, knownWord):
    # create no letters list
    noLetters = []
    for char in guessedLetters:
        if char not in knownWord:
            noLetters.append(char)

    newList = []
    for word in currentList:
        #make sure the wod doesn't contain no letters
        clear = True
        for noLetter in noLetters:
            if noLetter in word:
                clear = False

        # it passed the no letters test
        if clear:
            if doesWordMatch(word, knownWord):
                newList.append(word)

    return newList

def solveWord(wordDictionary, hangman):
    wordSize = hangman.getWordLength()
    possibleWords = wordDictionary.getWordList(wordSize)
    guessedLetters = []
    knownWord = "*" * wordSize

    # makes guesses based on letters guessed
    # for i in range(7):
    while not hangman.isSolved():
        #make guess
        letter = getHighestLetterCount(possibleWords, guessedLetters)
        guessedLetters.append(letter)
        knownWord = hangman.makeGuess(letter)
        possibleWords = updatePossibleList(possibleWords, guessedLetters, knownWord)


    # print(guessedLetters)
    return hangman.getGuessCount()

wordDictionary = WordDict()


textFile = open("wordsEn.txt","r")
fullText = textFile.read()
textFile.close()


wordList = fullText.split("\n")
for i in range(len(wordList)):
    wordList[i] = wordList[i].lower().replace("'","")    

total = 0.0
count = 1000
for i in range(count):
    word = wordList[randrange(len(wordList))]
    hangman = Interface(word)
    guesses = solveWord(wordDictionary, hangman)
    if guesses > 7:
        print(word)
    total += guesses

print(total/count)