import nltk
import random
from nltk.corpus import words
wordList = words.words();
customList = []
done = False
useCustomList = True

print("Welcome to Hangman")
if (input("Warning: you can not change you answer\nif you do not add anything to a the custom list the default list will be used instead\nWould you like to use a custom list(y/n): ") == "y"):
    print("Using Custom List, Please make sure to add words")
    useCustomList = False

def play(hangmanOutput):
    exit = False
    win = False
    guesses = 0
    while not exit:
        #gets user input
        userGuess = input("Please guess a letter or the word: ")
        #if user guesses word
        if userGuess == secretWord:
            win = True
            exit = True
            guesses += 1
        #if user guesses letter
        elif secretWord.find(userGuess[0:1]) > -1:
            print("Letter found")
            NewhangmanOutput = toString(secretWord,hangmanOutput, userGuess)
            hangmanOutput = NewhangmanOutput
            outputToString(hangmanOutput)

        #user guess incorrect
        else:
            guesses += 1
            print("Incorrect")
            outputToString(hangmanOutput)

        #user hit max guesses
        if (guesses == 6):
            exit = True
            print("guesses maxed, the correct word was: ", secretWord)
        
        if (hangmanOutput == secretWord):
            win = True
            exit = True
            
    #print statement for win/lose
    if win:
        print("Congrat's you guessed the word")
    else:
        print("Better try next time")
def startToString(word):
    output = ""
    for x in range(len(word)):
        print("_ ",end = "")
        output += ("_")
    
    print()
    return(output)

def outputToString(word):
    newWord = ''
    for x in range(len(word)):
        newWord += word[x] + ' '
    
    print(newWord)
   

#work in progress
def toString(secretWord, past, guess):
    for x in range(len(past)):
        if (secretWord[x] == guess):
            past = past[:x] + guess + past[x+1:]
    return(past)
    
    
while not done:
    print("\n0. Quit")
    print("1. Play")
    print("2. add custom word")
    print("3. add to custom list")
    userInput = input("Please pick your Selection: ")
    
    if userInput == "1":
        #sets up game
        index = random.randint(0,len(wordList)-1);
        secretWord = wordList[index]
        secretLength = len(secretWord)
        
        print("The random word is ", secretLength, "letters long")
        hangmanOutput = startToString(secretWord)
        play(hangmanOutput)

        #adds new word
    elif userInput == "2":
        newWord = input("Please enter your word: ")
        if newWord in wordList:
            wordList.append(newWord)
            print("word added\n")
        else:
            print("word already in list\n")
    elif userInput == "3":
        if useCustomList:
            customList.append(input("Enter a word: "))
            wordList = customList
        else:
            print("Warning you're currently not using the custom list")
    elif userInput == "0":
        done = True
    else:
        print("Invalid Selection\n")
            
           
