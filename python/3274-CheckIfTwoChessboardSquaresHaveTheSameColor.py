'''
3274. Check if Two Chessboard Squares Have the Same Color
Easy
Topics
premium lock icon
Companies
Hint
You are given two strings, coordinate1 and coordinate2, representing the coordinates of a square on an 8 x 8 chessboard.

Below is the chessboard for reference.



Return true if these two squares have the same color and false otherwise.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first (indicating its column), and the number second (indicating its row).

 

Example 1:

Input: coordinate1 = "a1", coordinate2 = "c3"

Output: true

Explanation:

Both squares are black.

Example 2:

Input: coordinate1 = "a1", coordinate2 = "h3"

Output: false

Explanation:

Square "a1" is black and "h3" is white. 
'''
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        ascii1 = ord(coordinate1[0])
        ascii2 = ord(coordinate2[0])

        int1 = int(coordinate1[1])
        int2 = int(coordinate2[1])

        if (ascii1 % 2 == 0 and int1 % 2 == 0) or (ascii1 % 2 == 1 and int1 % 2 == 1):
            square1 = True
        else:
            square1 = False
        
        if (ascii2 % 2 == 0 and int2 % 2 == 0) or (ascii2 % 2 == 1 and int2 % 2 == 1):
            square2 = True
        else:
            square2 = False

        return not (square1 ^ square2)
def main():
    solution = Solution()
    print(solution.checkTwoChessboards("a1", "a3"))

main()