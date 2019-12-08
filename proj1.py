# File:        proj1.py
# Author:      De'Shaunna Scott
# Date:        11/3/15
# Section:     29
# Email:       dscott6@umbc.edu
# Description: This program will use a series of functions to simulate Conway's Game of life with a 2D
#              matrix

import copy
DEAD  = "."
ALIVE = "A"

# gets the number of rows and columns for the dimensions of the board
# Input: 
# Output: the dimesions of the board the user want to create
def getDimensions():

    row = int(input("Please enter number of rows:    "))
    # checks for valid row input
    while(row <=0):
        print("\tThat is not a valid value; please enter a number greater than or equal to 1")
        row = int(input("Please enter number of rows:    "))

    col = int(input("Please enter number of columns: "))
    # check for valid column input
    while(col <=0):
        print("\tThat is not a valid value; please enter a number greater than or equal to 1")
        col = int(input("Please enter number of columns: "))

    return[row,col]

# gets the cells the user wants to make alive and stores them in a list
# Input: user-specified dimensions of the board
# Output: the living cells as defined by the user
def getLivingCells(row,col):
    liveCells = []
    cellList = []
    print()

    liveRow  = input("Please enter the row of a cell to turn on (or q to quit): ")    
    # continuously asks the user for living cells until the user want to quit
    while(liveRow != "q"):
        # checks if the input for the row to turn on is valid then asks for a valid number
        while((int(liveRow) < 0) or ((int(liveRow) >= row))):
            print("\tThat is not a valid value; please enter a number between 0 and", row - 1,"inclusive...")
            liveRow = input("Please enter the row of a cell to turn on (or q to quit): ")
        cellList.append(int(liveRow))
        
        liveCol = int(input("Please enter a column for that cell: "))
        # check if the input for the column to turn on is valid then asks for a valid number
        while((liveCol < 0) or (liveCol >= col)):
            print("\tThat is not a valid value; please enter a number between 0 and", col - 1,"inclusive...")
            liveCol = int(input("Please enter a column for that cell: "))
        cellList.append(liveCol)

        # takes the cell list and appends it to live cells to create a list of lists to be used in 
        # the getBoard function
        liveCells.append(cellList)
        cellList = []
        print()
        liveRow  = input("Please enter the row of a cell to turn on (or q to quit): ")
    return liveCells

# determines how many generations the user wants to run
# Input:
# Output: number of time the game will run
def iterations():
    print()
    iteration = int(input("How many iteratons should I run? "))

    # makes sure the value given is valid 
    while(iteration < 0):
        print("\tThat value is invalid, please enter a value greater than 0")
        iteration = int(input("How many iteration should I run? "))
    return iteration

# gets the information for the starting board and changes the specified cells to alive
# Input: dimensions and living cells
# Output: the starting game board
def getBoard(row,col,liveCells):
    board  = []

    # the nested for loop creates temporary board and converts it into a list in order to create a 
    # blank board
    tempBoard = ""
    for r in range(row):
        for c in range(col):
            tempBoard += DEAD
        board.append(list(tempBoard))
        tempBoard = ""
    
    # loops through the live cells list to set each user-specified cell to alive
    for loc in liveCells:
        board[loc[0]][loc[1]] = ALIVE 
    
    return board

# takes in the current board and changes its contents based on game rules for the next generation
# Input: the current board of the game
# Output: the board changes based on game rules
def nextGeneration(board):
    board2 = copy.deepcopy(board)
    # loops over the copied list
    for r in range(len(board)):
        for c in range(len(board[r])):
            livingCells = 0
    
            # checks if the surrounding cells of a particular cell are alive and determines what to do
            # with that cell in the next generation
            if (r - 1 >= 0) and (c - 1 >= 0):
                if board2[r - 1][c - 1] == ALIVE:
                    livingCells += 1
            
            if (c - 1 >= 0):
                if board2[r][c - 1] == ALIVE:
                    livingCells += 1

            if (r - 1 >= 0):
                if board2[r - 1][c] == ALIVE:
                    livingCells += 1

            if (c + 1) < len(board2[r]):
                if board2[r][c + 1] == ALIVE:
                    livingCells += 1
            
            if ((r + 1) < len(board2)):
                if board2[r + 1][c] == ALIVE:
                    livingCells += 1

            if (r + 1) < len(board2):
                if board2[r + 1][c - 1] == ALIVE:
                    livingCells += 1

            if (r + 1 < len(board2) and c + 1 < len(board2[r])):
                if board2[r + 1][c + 1] == ALIVE:
                    livingCells += 1
            
            if (r - 1 >= 0) and (c + 1 < len(board2[r])):
                if board2[r - 1][c + 1] == ALIVE:
                    livingCells += 1

            # next three block of ifs check the rules of the game to see if that cell lives or dies
            if board2[r][c] == ALIVE:
                if livingCells < 2 or livingCells > 3:
                    board[r][c] = DEAD
            
            if board2[r][c] == ALIVE:
                if livingCells == 2 or livingCells == 3:
                    board[r][c] = ALIVE

            if board2[r][c] == DEAD:
                if livingCells == 3:
                    board[r][c] = ALIVE

    return board

# takes in the current board and displays the content of the board
# Input: the current game board
# Output: the contents of the board 
def displayBoard(board):
    for line in board:
        print("".join(line))

# acts as the main driver of the program and calls the needed functions
def main():
    [row,col] = getDimensions()
    liveCells = getLivingCells(row,col)  
    iteration = iterations()
    currentBoard = getBoard(row,col,liveCells)
    iterationNum = 1
    print()
    print("Starting Board:")
    displayBoard(currentBoard)

    # runs the game the amount of times the user wants it to run
    for i in range(iteration):
        board = nextGeneration(currentBoard)
        print("Iteration", iterationNum,":")
        displayBoard(board)
        iterationNum += 1
main()
