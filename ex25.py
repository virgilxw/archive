def break_word(stuff):
    """This function will break up word for us. IT MUST DOUBLE QUOTATION MARKS IN .SPLIT("")"""
    word = stuff.split(" ")
    return word

def sort_word(word):
	#Sorts the word.
	return sorted(word)
	
def print_first_word(word):
	#Prints the first word after popping it off
	word = word.pop(0)
	print word

def print_last_word(word):
	#Prints the last word after popping it off
	word = word.pop(-1)
	print word
	
def sort_sentence(sentence):
	#Takes in a full sentence and returns sorted word
	word = break_word(sentence)
	return sort_word(word)
	
def print_first_and_last(sentence):
	#Prints the first and last word of the sentence
	word = break_word(sentence)
	print_first_word(word)
	print_last_word(word)
	
def print_first_and_last_sorted(sentence):
	#sorted the word then prints the first and last one.
	word = sort_sentence(sentence)
	print_firstword(word)
	print_last_word(word)