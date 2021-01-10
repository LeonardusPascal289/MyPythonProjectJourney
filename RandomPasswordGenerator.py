# creating a Ranmdom Passwaord

import random
import string
# adding directiry to file given
import os.path

def displayInterface():
    print('Hello and welcome to Random Password Generator')
    letterLength = int(input('How Many Letters do you want :' ))
    digitsLength = int(input('How Many Digits do you want : '))
    # /optional adding a symbol
    optionSymbol= input('Do you want to add symbol (y/n): ')
    if optionSymbol =="Y" or optionSymbol== "y":
        randomPassword = addSymbol(letterLength,digitsLength) 
    elif optionSymbol =="N" or optionSymbol== "n":
        randomPassword=noSymbol(letterLength,digitsLength)
        
    else:
        print("you mistyped")
    # creating the List consisting of Password base on the User Choice 
    finalResult(randomPassword)

def finalResult(randomPassword):
    # checking character less than 8
    if len(randomPassword)<8:
        print('Password have to be at least 8 characters')
        displayInterface()
    else:
    # JOIN AND SHUFFLE PASSWORD
        random.shuffle(randomPassword)
        newPassword = "".join(randomPassword)
        print('Here is your new Random Password: ' + newPassword)
        saveToText(newPassword)

    
# Adding a Symbol or no option
def addSymbol(letterLength,digitsLength):
     symbolLength = int(input('How Mnay Symbol do you want : '))
     randomPassword = [random.choice(string.ascii_lowercase ) for i in range(letterLength)]
     randomPassword += [random.choice(string.digits ) for i in range(digitsLength)]
     randomPassword += [random.choice(string.punctuation ) for i in range(symbolLength)]
     return randomPassword

def noSymbol(letterLength,digitsLength):
     randomPassword = [random.choice(string.ascii_lowercase ) for i in range(letterLength)]
     randomPassword += [random.choice(string.digits ) for i in range(digitsLength)]
     return randomPassword


# a fucntion that will save the new passord into a .txt file
def saveToText(newPassword):
    absPath= 'C:\\Users\\ACER\\Desktop\\PasswordGenerator'
    nameOfFile = input(" Name of the Password: ")
    newFile = os.path.join(absPath,nameOfFile+".txt")
    # opening and writing the newPassword created
    file1= open(newFile,"w")
    file1.write("Your new random password : "+newPassword)
    file1.close()
    print(" Your new password have been save to {pathname}".format(pathname = newFile))
 

displayInterface()