#---------------------------
#Flash Cards by Aaron Porter
#---------------------------
#v1.0 10/22/2016
#---------------------------

#---------
#-imports- 
#---------
import random
import os

#continue option presest to run
cont = "1"
#prints out the file options within directory
directory = os.listdir()
print("Here are the text files to load.")
print("-"*40)

for item in directory:
        if ".txt" in item:
                print(item)
                print("-"*40)
                
#Makes user input a correct file
while True:
        #attempt to open and read the file
        try:
        
            file = open(input("Which file of slides would you like to use? "),"r")
            contents = file.readlines()
            file.close()
            break
        
        except:
            print("That file does not appear to be there, try again!")
            print("Make sure to add .txt to you file name.")
#continues looping til user quits
while True:


        #dictionary for each term
      flashcards = {}
      #spliting terms based on the hyphen and setting definition
      for line in contents:
            line = (line.strip()).split(" - ")
            flashcards[line[0]] = line[1]
        #continue option to only run through options missed
      if cont == "2":
            notAnswered = list(personalized_deck.keys())
        #otherwise use regular deck
      else:
            notAnswered = list(flashcards.keys())
        #creates empty lists of wrong and correct 
      wrong = []
      correct = []
      #runs through not answered questions
      while notAnswered:
              #picks a random question
            currentQuestion = random.choice(notAnswered)
            print("You have", len(notAnswered), "questions remaining.")
            answer = input("What is the definition of "+ currentQuestion +" ? : ")
            #a way to break out before anwering all questions
            if answer == "RoSeBuD":
                  break
                #if correct add it to correct and remove it from not answered
            elif answer.upper() == flashcards[currentQuestion].upper():
                  correct.append(currentQuestion)
                  notAnswered.remove(currentQuestion)
                  print("You got it! Only", str(len(notAnswered)), "left!")
                  #if wrong add it to wrong and remove it from not answered
            else:
                  wrong.append(currentQuestion)
                  notAnswered.remove(currentQuestion)
                  print("Sorry thats incorrect. Only", str(len(notAnswered)), "left!")
        #creates a slide deck of missed ones
      personalized_deck = {}
      for item in wrong:
            personalized_deck[item] = flashcards[item]
      print( "You scored", str(len(correct)), "//", str(len(correct)+len(wrong)),"!")

        #different continue options
      while True:    
            print( "Type 1 to play again with the full deck.")
            print( "Type 2 to play with the ones you missed.")
            print( "Type 3 to review your missed flashcards.")
            print( "Type 4 to play with a different slide deck.")
            print( "Type 5 to save a your incorrect cards.")
            print( "Type 6 to quit.")
            cont = input ( "Please type your answer: ")
            #loops back to the top of program
            if cont == "1" or cont == "2":
                  break
            #prints out the ones you missed with the definitions
            if cont == "3":
                  print()
                  print("These are the ones you missed")
                  print("-"*40)
                  for item in wrong:
                        print(item, "means", flashcards[item])
                  print("-"*40)
                  print()
            #prints the user with the files in the directory so as
            #to give them the ability to choose a new file
            if cont == "4":
                  directory = os.listdir()
                  print("Here are the text files to load.")
                  print("-"*40)

                  for item in directory:
                        if ".txt" in item:
                              print(item)
                              print("-"*40)
                  while True:
                        try:
                              file = open(input("Which file of slides would you like to use? "),"r")
                              contents = file.readlines()
                              file.close()
                              break
                        except:
                              print("That file does not appear to be there, try again!")
                              break
                  break
            #users can save their incorrect slides to come back to at a later date
            if cont == "5":
                  while True:
                        print("What would you like to save your incorrect slides as?")
                        save = input("(Please remeber to add .txt to the end of your save name!) ")
                        overwrite =""
                        if save in directory:
                              print("It appears that there is already a file with that name.")
                              overwrite = input("Would you like to overwrite this file? Y/N")
                        if overwrite.upper() == "Y" or not overwrite:
                              while True:
                                    try:
                                          file = open(save,"w")
                                          for item in wrong:
                                                file.write(item + " - " + flashcards[item]+"\n")
                                          file.close()
                                          saved = True
                                          print("File Saved as", save +"!")
                                          print()
                                          break
                                    except:
                                          print("There seems to be an error writing to that file. \n Please try again.")
                                          print()
                                          break
                        if saved == True:
                              break
                        else:
                              areYouSure = input("Do you still want to save? Y/N ")
                        if areYouSure.upper() == "N":
                          break
            #the ability to quit
            if cont == "6":
                  break
            else:
                  print("Please select from the following options!")
      if cont == "6":
            break



