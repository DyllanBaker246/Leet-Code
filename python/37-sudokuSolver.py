'''
37. Sudoku Solver
Hard
Topics
premium lock icon
Companies
Hint
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
'''
from unittest.mock import patch
import sys

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        print(self.solveElement(board, 0, 0))
    
    def solveElement(self, board: list[list[str]], row: int, col: int) -> bool:
        i = 0
        if row == 9:
            return True
        while i < len(board):
            j = 0
            while j < len(board[i]):
                if not (board[i][j] == "."):
                    j += 1
                    continue
                arr = self.getPossibleValues(board, i, j)
                if len(arr) == 0:
                    # board[i][j] == "."
                    return False
                k = 0
                while k < len(arr):
                    board[i][j] = arr[k]
                    
                    for item in arr:
                        print(item, end=' ')
                    print("")
                    print("Current Location:",i, j)
                    print("")
                    printMatrix(board)
                    print("")

                    if self.solveElement(board, i, j):
                        return True
                    board[i][j] = "."


                    k += 1
                return False

                j += 1

            # if i == 8:
            #     sys.exit()
            i += 1
        return True
    
    
    # finding possible values
    def getPossibleValues(self, board: list[list[str]], row: int, col: int) -> list[str]:
        possibleVals = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        # take away values from row
        i = 0
        while i < len(board[row]):
            try:
                index = possibleVals.index(board[row][i])
            except ValueError:
                index = -1
            if not (index == -1):
                del possibleVals[index]
            i += 1

        # take away values from subBox
        subBoxCoordinates = self.getBoxCoordinates(row, col)
        i = 0
        while i < 3:
            j = 0
            while j < 3:
                try:
                    index = possibleVals.index(board[i + subBoxCoordinates[0]][j + subBoxCoordinates[1]])
                except ValueError:
                    index = -1
                if not (index == -1):
                    del possibleVals[index]
                j += 1
            i += 1
        
        # take away values from column
        i = 0
        while i < len(board):
            try:
                index = possibleVals.index(board[i][col])
            except ValueError:
                index = -1
            if not (index == -1):
                del possibleVals[index]
            i += 1
        return possibleVals

    def getBoxCoordinates(self, row: int, col: int) -> list[int]:
        # given a possition in the board, return the top left
        # coordinate of the sub box
        # 0 1 2
        # 3 4 5
        # 6 7 8
        
        # Sub boxes 0, 1, 2
        if row >= 0 and row <=2:
            if col >= 0 and col <= 2:
                return [0,0]
            if col >= 3 and col <= 5:
                return [0,3]
            if col >= 6 and col <= 8:
                return [0,6]

        # Sub boxes 3, 4, 5
        if row >= 3 and row <= 5:
            if col >= 0 and col <= 2:
                return [3,0]
            if col >= 3 and col <= 5:
                return [3,3]
            if col >= 6 and col <= 8:
                return [3,6]

        # Sub boxes 6, 7, 8
        if row >= 6 and row <= 8:
            if col >= 0 and col <= 2:
                return [6,0]
            if col >= 3 and col <= 5:
                return [6,3]
            if col >= 6 and col <= 8:
                return [6,6]

        return [-1,-1]
            
        
        

def printMatrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            print(matrix[i][j], end = ' ')
            j += 1
        print("")
        i += 1

# main ----------------------------------
def main():
    solution = Solution()
    board1 = [["5","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]]

    print(solution.solveSudoku(board1))


    # printMatrix(board1)

main()
        



