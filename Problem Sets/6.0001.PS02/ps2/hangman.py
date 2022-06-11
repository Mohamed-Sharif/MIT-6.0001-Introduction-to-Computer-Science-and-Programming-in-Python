# Problem Set 2, hangman.py

# Hangman Game
# -----------------------------------

# Starting by imporing the required modules
import random
import string
import numpy

#  Creating a function to read the words.txt file into a list of words
def load_words():
    """
    Reading all the words from a txt file
    Returns wordlist : list containing all words in the file

    """
    print("Loading word list from file...")
    with open ('words.txt','r') as f:
        lines = f.readline()
        wordlist = lines.split()
        print("   {} words loaded.".format (len(wordlist)))
    return wordlist

# Loading the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

# Let the game begin with the computer choosing a word randomly
def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)




# Identifying helper fucntions
# Those functions should be used with the hangman function game 

# Using this function to see if the word is guessed correctly or not
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in range(len(secret_word)):
        if not secret_word[i] in letters_guessed:
            return False
    return True       

# For test purposes
# secret_word = 'apple' 
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
# print(is_word_guessed(secret_word, letters_guessed)) 

# using this function to show the user's the guessed words
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = []
    for i in range (len(secret_word)):
        guessed_word.append("_ ")
        if secret_word[i] in letters_guessed:
            guessed_word[i] = secret_word[i] 
    return "".join(guessed_word)

# For test purposes
# secret_word = 'apple'  
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
# print(get_guessed_word(secret_word, letters_guessed))             


# Using this function to show the user's the letters he hadn't chosen yet
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    available_letters = list(filter(lambda v: v not in letters_guessed,
                                    all_letters))
    return "".join(available_letters)

# For test purposes
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
# print (get_available_letters(letters_guessed)) 


# The first edition of the game without hints
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, the user gets to know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user starts with 6 guesses

    * Before each round, the user knows how many guesses
      s/he has left and the letters that s/he has not yet guessed.
    
    * The user is to supply one guess per round.
    
    * The user receives feedback immediately after each guess 
      about whether the guess appears in the computer's word.

    '''
    # Starting by identifying the needed variables
    wordlength = len(secret_word)
    numguess= 6
    warnings=3
    letters_guessed= []
    gameround = 0
    iswordguessed= is_word_guessed(secret_word, letters_guessed)

    
    # Giving the user the length of the word as well as the initial number of guesses
    print("Welcome to the game Hangman!")
    print ("I am thinking of a word that is {} letters long ".format(wordlength))
    print ( " --------------------- ----------------------")

    # Game round: each round consists of asking the user to guess a letter
    # Tell the user whether the letter appears on the word or not
    # give the users the number of the guesses left
    
    while not iswordguessed and numguess > 0:
        availableletters= get_available_letters(letters_guessed)
        guessedword = get_guessed_word(secret_word, letters_guessed)
        gameround +=1
        print("Round: ",gameround)
        print ("You have {} guesses left".format (numguess))
        print ("Available letters:" + availableletters) 
        guessed_letter = input("Please guess a letter: ").lower()

        # Checking the user's input to be alphapetical and only one letter
        warningscheck = not guessed_letter.isalpha() or (len(guessed_letter) > 1
                                            or guessed_letter in letters_guessed)
        
        letters_guessed.append (guessed_letter)

        if  warningscheck:
            if warnings >0:
                warnings -=1
                print("Oops! That is not a valid letter. You have {} warnings left".format (warnings) 
                      + guessedword)
            else:
                numguess -=1
                print("Oops! That is not a valid letter. You lost a guess")
        
        elif guessed_letter in secret_word:
            letters_guessed.append (guessed_letter)
            guessedword = get_guessed_word(secret_word, letters_guessed)
            print ('Good guess: ' + guessedword)
        
        elif guessed_letter in ['a','e','i','o','u']:
            numguess -=2
            print ('Oops! That letter is not in my word: ' + guessedword)
        
        else:
            numguess -=1
            print ('Oops! That letter is not in my word: ' + guessedword)
        
        # Updating the game to check if the word is guessed
        iswordguessed= is_word_guessed(secret_word, letters_guessed)

    # Terminating the game with the user either losing or winning
    if numguess <= 0:
        print("Game over")
        print("The secret word is " + secret_word)
    # Calculating the total score by counting the unique letters
    # in the secret word and multiply it with the guesses left
    else:
        totalscore = numguess * len(numpy.unique(list(secret_word)))
        print("Wow You guess it right indeed it is " + secret_word)
        print ("Congrats your score is {} points".format(totalscore))


# Other helper functions for the second edition of the game with hints 
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    trimmedword=my_word.replace("_ ", "_").strip()
    for i in range(len(trimmedword)):
        if (len(trimmedword) != len(other_word)
            ) or (trimmedword[i] != other_word[i] and trimmedword[i] != '_'):
            return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
           matches.append(word)
    if len (matches) != 0:
        return matches
    else:
        return "No matches found"
        



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    wordlength = len(secret_word)
    numguess= 6
    warnings=3
    letters_guessed= []
    gameround = 0
    iswordguessed= is_word_guessed(secret_word, letters_guessed)

    
    # Giving the user the length of the word as well as the initial number of guesses
    print("Welcome to the game Hangman!")
    print ("I am thinking of a word that is {} letters long ".format(wordlength))
    print ( " --------------------- ----------------------")

    # Game round: each round consists of asking the user to guess a letter
    # Tell the user whether the letter appears on the word or not
    # give the users the number of the guesses left
    while not iswordguessed and numguess > 0:
        availableletters= get_available_letters(letters_guessed)
        guessedword = get_guessed_word(secret_word, letters_guessed)
        gameround +=1
        
        print("Round: ",gameround)
        print ("You have {} guesses left".format (numguess))
        print ("Available letters:" + availableletters) 
        guessed_letter = input("Please guess a letter: ").lower()

        warningscheck = ((not guessed_letter.isalpha()) or (
                                 len(guessed_letter) > 1
                                 ) or (guessed_letter in letters_guessed)
                                 ) and (guessed_letter != '*')
        
        letters_guessed.append (guessed_letter)
        
        # Checking the user's input to be alphapetical and only letter
        if  warningscheck:
            if warnings >0:
                warnings -=1
                print("Oops! That is not a valid letter. You have {} warnings left".format (warnings) 
                      + guessedword)
            else:
                numguess -=1
                print("Oops! That is not a valid letter. You lost a guess")
        
        elif guessed_letter == '*':
            print(show_possible_matches(guessedword))
            
        elif guessed_letter in secret_word:
            guessedword = get_guessed_word(secret_word, letters_guessed)
            print ('Good guess: ' + guessedword)
        
        elif guessed_letter in ['a','e','i','o','u']:
            numguess -=2
            print ('Oops! That letter is not in my word: ' + guessedword)
        
        else:
            numguess -=1
            print ('Oops! That letter is not in my word: ' + guessedword)
    
        iswordguessed= is_word_guessed(secret_word, letters_guessed)
    
    # Terminating the game with the user either losing or winning
    if numguess <= 0:
        print("Game over")
        print("The secret word is " + secret_word)
    # Calculating the total score by counting the unique letters
    # in the secret word and multiply it with the guesses left
    else:
        totalscore = numguess * len(numpy.unique(list(secret_word)))
        print("Wow You guess it right indeed it is " + secret_word)
        print ("Congrats your score is {} points".format(totalscore))

    

# For test purposes
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

# For test purposes
if __name__ == "__main__":

# Testing the hangman funciton only
#Uncomment to test and comment the uncommented two lines below   
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
# Testing the hangman with hints function    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
