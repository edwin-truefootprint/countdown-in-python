print('Welcome to Countdown')
print('Given 6 numbers, try to make the target. \nEnter an expression, or \n? for a hint, or \ng to give up and have the computer try, or \nr for reset, \nu for undo last step, or \nroman for switching to roman numerals, or \nnormal to stop roman numerals.\n')

# some standard modules we need
import readline
import math

#we also need 2 of our own 
import roman  # Roman numerals
import solver # an algorithm to solve the numbers game

# how we present numbers depends on the mode: maybe user wants to see Roman numerals
def stringNumbers(n):
    if inRoman:
        return roman.roman(obj)
    else:
        return str(n)

# by default not Roman numerals
inRoman=False
helpPrompt='But first, type ita if you want the target displayed in Roman numerals: '
line = input(helpPrompt)
if line == 'ita':
    inRoman=True

# first we need to find 6 random numbers from the list of 15 possible numbers
possibleNumbers=[1,2, 3,4,5,6,7,8,9,10,20,25,50,75,100]
from random import randrange
numberOfNumbers=len(possibleNumbers) # should be 15 elements in list
totalNumbersNeeded=6
chosenNumbers=[] # one by one we will add random elements from the possibleNumbers
for i in range(totalNumbersNeeded):  # 6 times we will pick a random element
    r=randrange(numberOfNumbers) # returns an int between 0 and 14, which are valid indices in the possibleNumbers list
    chosenNumbers.append(possibleNumbers[r])
print('The 6 random numbers are:')
print (chosenNumbers)

# now we randomly pick the target
target=randrange(101,1000) #some random number between 101 and 999
print('Try to make',stringNumbers(target), 'using + - * and /')


# now we're asking the user to enter an expression, or a specific command
# first a few initialisations
giveUp=False
workingNumbers=chosenNumbers.copy() #make a copy in case we need to reset
previousWorkingNumbers=workingNumbers.copy()  # prepare for undo last step

# now the big loop to keep asking for expressions, each time reducing the list of numbers
while (len(workingNumbers) > 1) and (not giveUp):
   helpPrompt='Enter expression: (for instance ' + str(workingNumbers[0]) + '+' + str(workingNumbers[1]) +'): '
   line = input(helpPrompt)
   if line == 'r':
        workingNumbers=chosenNumbers  # reset the whole thing
        print(workingNumbers, 'target=', stringNumbers(target))
   elif line == 'u':
        workingNumbers=previousWorkingNumbers  # undo: reset to previous set of numbers
        print(workingNumbers, 'target=', stringNumbers(target))
   elif line == '?':
        askForHint = True 
        isPossible=solver.canItBeDone(chosenNumbers,target,askForHint,'') # give hint for original problem, not the working set the user got to
        if not(isPossible):
            print('It can not be solved')
   elif line == 'g':
        giveUp=True
        askForHint = False
        solution=''
        isPossible=solver.canItBeDone(chosenNumbers,target,askForHint,solution) # give solution for original problem, not the working set the user got to
        if not(isPossible):
            print('It can not be solved')  
   elif line == 'roman':
        inRoman=True
        print(workingNumbers, 'target=', stringNumbers(target)) 
   elif line == 'normal':
        inRoman=False
        print(workingNumbers, 'target=', stringNumbers(target))
   else:
       # time to check a bit if this is valid expression
       operatorString='+-*/'
       for i in range(len(operatorString)):
          operator=operatorString[i]
          if operator in line:   # not a very good check, eg '1 2 +' will pass, but should not. FIX LATER
             # now check if the numbers used were valid
             splitList=line.split(operator)
             op1=int(splitList[0])
             op2=int(splitList[1])
             try:
                 index1=workingNumbers.index(op1) # surely the user picked an existing number (if not, handle exception below)
                 previousWorkingNumbers=workingNumbers.copy()  # prepare for undo last step
                 workingNumbers.remove(op1)
                 try:
                     index2=workingNumbers.index(op2)
                     workingNumbers.remove(op2)
                     result=int(eval(line)) # LATER: check if remainder is 0 for / and if result is positive for -
                     if result==target:
                         workingNumbers=[target]  # this will exit the while loop and signal success
                     else:
                        workingNumbers.append(result) # the result can be used for further calculations
                        print (workingNumbers, 'target=',stringNumbers(target))
                 except ValueError:
                     # element not found in list
                     print('Cheating:',op2)
                     workingNumbers=chosenNumbers.copy()  # reset the whole thing
                     previousWorkingNumbers=workingNumbers.copy()  # prepare for undo last step
                     print(workingNumbers, 'target=', stringNumbers(target))
             except ValueError:
                 # element not found in list
                 print('Cheating:',op1)
                 workingNumbers=chosenNumbers.copy() # reset the whole thing
                 previousWorkingNumbers=workingNumbers.copy()  # prepare for undo last step
                 print(workingNumbers, 'target=',stringNumbers(target))

if workingNumbers[0]==target:
     print('YES, you did it:',stringNumbers(target))
elif not giveUp:
    print('Sorry, you failed to make', stringNumbers(target), ' by', stringNumbers(int(math.fabs(workingNumbers[0] - target))))


# what if user wants to stop, as extra moves make it worse?
# what if the user wants to know if it can be done at all? without revealing answer?
# what if the user wants a hint?
# what if the user wants the computer to show how it can be done?
# what if user just made a typo instead of actually cheating? A reset is perhaps a bit harsh?









