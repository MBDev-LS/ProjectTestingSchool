import time
import sys

playerCodesFile = open('playerCodes.txt', 'r')
playerCodesList = playerCodesFile.read().split()
codeValid = 'non'
validationCache = 'nil'

failedLoginAttempts = 0
locks = 0

#print(playerCodesFile.read())
print(playerCodesList)

def CodeValidation(inputtedCode):
    print('User input:',inputtedCode)
    checkSuccess = False
    for i in range(len(playerCodesList)):
        if playerCodesList[i] == playerInputCode:
            print('Returning success!')
            return('success')
    if checkSuccess == False:
        return('failed')
    else:
        print('Error: Unexpected value in the checkSuccess function')
    
        
while codeValid != 'success':
    playerInputCode = input('Please enter your player code: ')
    codeValid = CodeValidation(playerInputCode)
    if codeValid == 'success':
        break
    elif codeValid == 'failed':
        failedLoginAttempts != 1
    elif codeValid == 'locked':
        locks += 1
    else:
        print("Error: Unexpected response from function.")

print("======================")
print("You entered the game!")
print("======================")
