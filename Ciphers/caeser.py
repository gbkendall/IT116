# Script Name: vigenere.py
# Description: A simple implementation of Caesar's Cipher
# Author: Gregory Kendall
# Last Updated: 9.23.2017

def whatFunction():
    function = input("Would you like to encrypt or decrypt your text?")
    if function in ('encrypt', 'decrypt'):
        return function
    else:
        print("Please type either 'encrypt' or 'decrypt'")

def whatMessage():
    message = input("\nPlease insert text to perform the cipher on: ")
    return message

def whatKey():
    key = 0
    while True:
        key = int(input("\nEnter the key would you like to choose (1-26): "))
        if (key >= 1 and key <= 25):
            return key

def translateMessage(function, message, key):
    strLength = int(len(message))
    x = 0
    translated = ''
    if function[0] == 'd':
        key = -key
    else:
        key = key
    while(x <= strLength):
        for symbol in message:
            if symbol.isalpha():
                num = ord(symbol)
                num += key
                if symbol.isupper():
                    if num > ord ('Z'):
                        num -= 26
                    elif num < ord ('A'):
                        num +=26
                elif symbol.islower():
                    if num > ord ('z'):
                        num -= 26
                    elif num < ord ('a'):
                        num +=26
                translated += chr(num)
                x = x + 1
            else:
                translated += symbol
                x = x + 1
        return translated

function = whatFunction()
message = whatMessage()
key = whatKey()

print("\nYour ciphered text is:")
print(translateMessage(function, message, key))
