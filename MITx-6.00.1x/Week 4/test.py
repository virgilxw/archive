#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    
    
    #test if word in wordlist
    if word in wordList:
        wordFreq = getFrequencyDict(word)
        for element in wordFreq:
            if hand[element] < wordFreq[element]:
                return False
        
        return True
        
    else:
        return False