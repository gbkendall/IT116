# Script Name: vigenere.py
# Description: A simple, prompted implementation of Vigenere's Cipher in python 3.6
# Author: Gregory Kendall
# Last Updated: 9.27.2017

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #global variable for the letters in the alphabet

def whatFunction():
    function = input("\nWould you like to encrypt or decrypt your text? ")
    if function in ('encrypt', 'decrypt'): #makes sure that the input mode is valid
        return function
    else:
        print("\nPlease type either 'encrypt' or 'decrypt'.")

def whatMessage():
    message = input("\nPlease insert text to perform the cipher on: ")
    return message

def whatKey():
    key = 0
    while True:
        key = input("\nEnter the keyword would you like to choose: ")
        if key.isalpha():
            return key
        else:
            print("Please enter only an alphabetic key.")

def translateMessage(key, message, function):
    translated = []
    keyIndex = 0
    key = key.upper()
    for symbol in message:
        num = ALPHABET.find(symbol.upper())
        if num != -1:
            if function == 'encrypt':
                num += ALPHABET.find(key[keyIndex])
            elif function == 'decrypt':
                num -= ALPHABET.find(key[keyIndex])

            num %= len(ALPHABET)
            if symbol.isupper():
                translated.append(ALPHABET[num])
            elif symbol.islower():
                translated.append(ALPHABET[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)

    return ''.join(translated)

function = whatFunction()
message = whatMessage()
key = whatKey()

print(translateMessage(key, message, function))
