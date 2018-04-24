#!/usr/bin/env python3
import random
import string
import os
allowed = set(string.ascii_letters)
uppercase = set(string.ascii_uppercase)

try:
# reading from a file
    file = open("wordbank.txt", "r")
    wordContainer = file.readlines()
    availableWords = []
    for i in range(0,len(wordContainer)):
        availableWords.append(i)

    file.close
    hiddenWord = ""

    # this runs until we run out of the words or the player says it is over
    gameIsOn = True
    while gameIsOn:
        roundIsOn = True
        # choosing the word from the word pool
        if len(availableWords) > 0:
            rand = availableWords[random.randint(0,len(availableWords)-1)]
            availableWords.remove(rand)
            hiddenWord = wordContainer[rand]

        # parsing the word
        visibleWord = ""
        ei = 0  # stands for effective index
        while ei < len(hiddenWord):
            if hiddenWord[ei] in allowed:
                if hiddenWord[ei] in uppercase:
                    hiddenWord[ei] = hiddenWord[ei].lower()
            else:
                hiddenWord = hiddenWord[0:ei] + hiddenWord[ei+1:len(hiddenWord)]
                ei = ei - 1
            ei = ei + 1

        for i in range(0, len(hiddenWord)):
            visibleWord = visibleWord + "_"
        lifes = 3
        doYouEvenPlayed = True
        if len(visibleWord) == 0:
            roundIsOn = False
            doYouEvenPlayed = False
        
        # this runs until the round is over
        while roundIsOn:
            # clear screen, show UI
            os.system('clear')
            showLifes = ""
            for i in range(0,lifes):
                showLifes = showLifes + " ❤"
            print(showLifes,'\n')
            showWord = ""
            for i in visibleWord:
                showWord = showWord + " " + i
            print(showWord, "\n\n")
            if hiddenWord == visibleWord:
                print("Congratulations, you've guessed the word!")
                roundIsOn = False
            
            # this runs if we haven't guessed the word yet
            if roundIsOn:
                # this runs until we deliver a letter
                while True:
                    letter = str(input("Type a letter: "))
                    if len(letter) == 1:
                        if letter in allowed:
                            if letter in uppercase:
                                letter = letter.lower()
                            break
                    print("That is not a letter!")

                # checking if the word contains a letter
                guessed = False
                for i in range(0,len(visibleWord)):
                    if hiddenWord[i] == letter:
                        visibleWord = visibleWord[0:i] + letter + visibleWord[i+1:len(visibleWord)]
                        guessed = True
                if guessed == False:
                    lifes = lifes - 1
                if lifes == 0:
                    print("You've lost all your chances. You are dead :(")
                    roundIsOn = False
            
        # checking if there are any words left to play with
        if len(availableWords) > 0 and doYouEvenPlayed:
            exitt = str(input("Do you want to play again? (type n to quit): "))
            if exitt == "n":
                gameIsOn = False
        if len(availableWords) == 0:
            print("Sorry, but I've run out of words. Thank you for playing!")
            gameIsOn = False
except IOError:
    print("An error occured while reading a word bank file.")