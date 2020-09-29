import os.path
from os import path
from Board import Board
import math
groupName = "Sigmoid"

def main():
    board = Board()
    result = PlayGame(board) #0 for tie, 1 for AI player wins, 2 for opposing player wins

#Function which will play the Gomoku game until completion
#board: An array represetnation of the game board
def PlayGame(board):
    #while not path.exists(groupName+".go"): #waits until it is the player's move
    #   pass
    if path.exists("endgame"):
        #end of game
        print("End of game")
        return 0
    else:
        #read opponent's move here
        if path.exists("move_file"):
            f = open("move_file").read()
            lines = f.split()
            row = LetterToNumber(lines[1])
            col = int(lines[2])
            board.placePiece(row, col, 0, 2) #makes opponent move
        #make move here
        PlayGame(board) #repeats until game completion

def MiniMax(inputPosition, inputDepth, inputMaximizingPlayer):

    #if the input depth is met or the game is over out put the evaluation of how good the move last made was
    if inputDepth == 0 or gameOver:
        return positionEval

    if inputMaximizingPlayer: #this is a boolean value
        maxEval = -math.INF

        for child in inputPosition:
            eval = MiniMax(child, inputDepth - 1, false)
            maxmaxEval = max(maxEval, eval)
            return maxEval
    else:
        minEval = math.inf
        for child in inputPosition:
            eval = MiniMax(child, depth - 1, true)
            minEval = min(minEval, eval)
            return minEval
   

def AlphaBetaPruning(inputPosition, inputDepth, inputAlpha, inputDeta, inputMaximizingPlayer):
    if inputDepth == 0 or gameOver:
        return positionEval

    if inputMaximizingPlayer: 
        for child in inputPosition:
            eval = Minimax(child, inputDepth - 1, false)
            maxEval = max(maxEval, eval) 

            alpha = max(alpha, eval)
            if beta <= alpha: 
                break

            return maxEval
    else:
        for child in inputPosition:
            eval = Minimax(child, inputDepth - 1, true)
            minEval = min(minEval, eval) 

            beta = max(beta, eval)
            if beta <= alpha:
                break
            return minEval

#------------------------------------------------------------------
#Heuristics that limit the depth to which the game tree is expanded

def CuttingOffSearch():
    return 1

def IterativeDeepening():
    return 1

def HeuristicContinuation():
    return 1


#------------------------------------------------------------------
#Heuristics that limit the branching factor of the game tree

def TaperedSearch():
    return 1

#------------------------------------------------------------------
#Big Boi Algorithm 
#https://en.wikipedia.org/wiki/Monte_Carlo_tree_search

def MonteCarloTreeSearch():
    return 1

#------------------------------------------------------------------
##Calcultes the utility for home team agent 
def CalculateSelfUtility():

    return 1

##Calcultes the utility for away team agent
def CalculateOpposingUtility():

    return 1

#------------------------------------------------------------------
##function to read in move_file to determind moves made from opposing agent 
def ReadFile():
    return 1

##inputCol is the number associated with the column 
#that the agent gives which NumberToLetter translates 
#into a capital letter associated with the number
#example: 1->A 
#         2->B
#         3->C
def NumberToLetter(inputColAsNumber):
    theLetter = chr(ord('@') + inputColAsNumber)
    return theLetter

##The opposite of NumberToLetter. It takes in a letter and converts it 
#into a number
def LetterToNumber(inputColAsLetter):
    theNumber = ord(inputColAsLetter) - ord('@')
    return theNumber

##function to output file with the move of our agent
#format: <groupname> <column> <row>
def OutputFile(inputRow, inputCol):
    f = open("move_file", "w")
    f.write("Sigmoid {} {}\n".format(inputCol, inputRow))
    f.close

    return f

main()
