import random
from IPython.display import clear_output

class Dice():
    __DIGlobalDiceMinFaces = 0
    __DIGlobalDiceMaxFaces = 0
    __DIHealthDiceMinFaces = 0
    __DIHealthDiceMaxFaces = 0
    __DIAttackDiceMinFaces = 0
    __DIAttackDiceMaxFaces = 0
    __DIDefenseDiceMinFaces = 0
    __DIDefenseDiceMaxFaces = 0
    
    def DiceInitiator(self):
        with open('Log/LogDices.txt', 'r') as DiceLog:
            DiceIndividualSettings = DiceLog.readline().split(".")
            self.__DIGlobalDiceMinFaces = int(DiceIndividualSettings[0].split("-")[0])
            self.__DIGlobalDiceMaxFaces = int(DiceIndividualSettings[0].split("-")[1])
            self.__DIHealthDiceMinFaces = int(DiceIndividualSettings[1].split("-")[0])
            self.__DIHealthDiceMaxFaces = int(DiceIndividualSettings[1].split("-")[1])
            self.__DIAttackDiceMinFaces = int(DiceIndividualSettings[2].split("-")[0])
            self.__DIAttackDiceMaxFaces = int(DiceIndividualSettings[2].split("-")[1])
            self.__DIDefenseDiceMinFaces = int(DiceIndividualSettings[3].split("-")[0])
            self.__DIDefenseDiceMaxFaces = int(DiceIndividualSettings[3].split("-")[1])

    def GlobalDice(self):
        #DiceFaces = 6
        Dice = (random.randint(self.__DIGlobalDiceMinFaces, self.__DIGlobalDiceMaxFaces))
        return Dice
    
    def DiceHealth(self):
        #DiceFaces = 15
        Dice = (random.randint(self.__DIHealthDiceMinFaces, self.__DIHealthDiceMaxFaces))
        return Dice
    
    def DiceAttack(self):
        #DiceFaces = 10
        Dice = (random.randint(self.__DIAttackDiceMinFaces, self.__DIAttackDiceMaxFaces))
        return Dice
    
    def DiceDefense(self):
        #DiceFaces = 10
        Dice = (random.randint(self.__DIDefenseDiceMinFaces, self.__DIDefenseDiceMaxFaces))
        return Dice
    
    def FirstPlayerTurn():
        DiceFaces = 2
        Dice = (random.randint(1,DiceFaces))
        return Dice
    
    def SetDices():
        pass
    
    def ResetDices():
        clear_output()
        open('Log/LogDices.txt', 'w').close
        with open('Log/LogDicess.txt', 'w') as DiceLog:
            DiceLog.write("1-6.3-15.1-10.1-10")