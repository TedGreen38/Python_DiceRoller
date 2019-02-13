'''
Ted Green
7/26/2018
Python DnD Dice Roller Challenge:
Concienved by user Jnazrio on the Daily Programmer reddit
'''

import random


class Dice:

    # initializes variables to be used within the class
    def __init__(self,diceNum:int,diceVal:int):
        self._diceNum = diceNum
        self._diceVal = diceVal

    def get_Roll(self):
        
        diceTotal = 0
    
        for rolls in range(self._diceNum):
            diceRoll = 0
            diceRoll = random.randint(1, self._diceVal)
            # adds value of diceRoll into diceTotal
            diceTotal += diceRoll
        # returns the value of diceTotal    
        return diceTotal
        
        
def main():

    # gets input from the user in the form of a string
    getInput = input("Please input how many dice you would like to roll along with its value (EX:2d4):")

    # seperates the input into a list that is seperated by a "d" character
    splitInput = getInput.split("d")

    # places the values of the splited input into its own variables
    # - diceNum = number of dice being rolled
    # - diceVal = number of sides on a single
    diceNum = int(splitInput[0])
    diceVal = int(splitInput[1])

        
    roll1 = Dice(diceNum,diceVal)

    # prints the results of the dice rolls
    print("The value you rolled with the", getInput, "is", roll1.get_Roll())


main()
