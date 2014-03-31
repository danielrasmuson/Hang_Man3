# gets the word dictionary from text file
# lower cases everythign
# removes non letters
import pickle
class WordDict(object):
    """docstring for WordDict"""
    def __init__(self):
        # self.setDictionary();
        # pickle.dump( self.wordDictionary, open( "pickleWordDictionary.p", "wb" ) )
        # pickle.dump( self.wordDictionary, open( "pickleWordDictionary.p", "wb" ) )
        self.wordDictionary = pickle.load(open("pickleWordDictionary.p", 'rb'))

    # def setDictionary(self, fileName="wordsEn.txt"):
    #     textFile = open(fileName, "r")
    #     fullText = textFile.read()
    #     textFile.close()

    #     self.wordDictionary = {}
    #     counter = 0
    #     for word in fullText.split("\n"):
    #         word = word.lower()
    #         cleanWord = ""
    #         for char in word:
    #             if 96 < ord(char) < 123:
    #                 cleanWord += char

    #         self.wordDictionary[cleanWord] = {"length": len(cleanWord)}

    def getLength(self, word):
        return self.wordDictionary[word]["length"]

    def getWordList(self, wordSize):
        """returns a list of words matching this size"""
        wordList = []
        for word in self.wordDictionary.keys():
            if self.getLength(word) == wordSize:
                wordList.append(word)
        return wordList