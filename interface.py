# This file will take in guesses are return the new word including that guess

class Interface(object):
    """docstring for Interface"""
    def __init__(self, word):
        self.word = word
        self.knownWord = len(word)*"*"
        self.guessCount = 0

    def makeGuess(self, letter):
        # increase the guess count
        if letter not in self.word:
            self.guessCount += 1

        # removes astrick over word if letter is in the word
        knownList = list(self.knownWord)
        for i in range(len(self.word)):
            if letter == self.word[i]:
                knownList[i] = self.word[i]

        # sets the new knowWord
        self.knownWord = "".join(knownList)
        return self.knownWord

    def isSolved(self):
        if "*" not in self.knownWord:
            return True
        else:
            return False

    def getGuessCount(self):
        return self.guessCount

    def getWordLength(self):
        return len(self.word)