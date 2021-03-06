def break_words(stuff): # this breaks words into a [ , , , ] list
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):# this puts words into a list [ , , , ,] in alphabetical order
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping off"""
    word = words.pop(0)# .pop(0) the 0 is using slicing to tell function what first word is
    print(word) #prints words.pop(0)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)#Pop pops you to end/last word via -1 slice
    print(word)#this prints the popped word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence) #this break the words into a list [ , , ]
    return sort_words(words)#this sorts broken words into alphabetical order

def print_first_and_last(sentence):
    """Print the first and last words of the sentence"""
    words = break_words(sentence)#this break the words into a list [ , , ]
    print_first_word(words)#prints first word in list
    print_last_word(words)#prints last word in list

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence) #uses function to break into list then sort in alphabetical worder
    print_first_word(words) #prints first word of sort_sentence
    print_last_word(words)#prints last word of sort_sentence
