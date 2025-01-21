import nltk
import random
from nltk.corpus import words
wordList = words.words();
done = False

print("Welcome to Hangman")

def play():
    exit = False
    win = False
    guesses = 0
    print(secretWord)
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
            guesses += 1
            print("Letter found")
        #user guess incorrect
        else:
            print("Incorrect")
            
        #user hit max guesses
        if (guesses == 6):
            exit = True
            print("guesses maxed, the correct word was: ", secretWord)
                
    #print statement for win/lose
    if win:
        print("Congrat's you guessed the word")
    else:
        print("Better try next time")

def toString():
    #show the user length of word using _ _ _ and show users where their letter was found
    #also add to play() if user guesses all letters to give them a win

    print("working...")

while not done:
    print("0. Quit")
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
        play()

        #adds new word
    elif userInput == "2":
        newWord = input("Please enter your word: ")
        if newWord in wordList:
            wordList.append(newWord)
            print("word added\n")
        else:
            print("word already in list\n")
    elif userInput == "3":
        print("in progress")
        
    elif userInput == "0":
        done = True
    else:
        print("Invalid Selection\n")
            
           
