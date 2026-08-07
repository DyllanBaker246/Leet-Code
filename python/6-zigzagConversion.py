'''
6. Zigzag Conversion
Medium
Topics
premium lock icon
Companies
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''
def printMatrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            print(matrix[i][j], end = ' ')
            j += 1
        print("")
        i += 1


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if only 1 row
        if numRows == 1:
            return s

        # Find muber of columns
        length = len(s)
        col = 0
        i = 0
        while length > 0:
            length = length - numRows
            col += 1

            # handles number of diagonal columns
            if length > 0:
                length = length - (numRows - 2)
                col += (numRows - 2)
        
        # create matrix
        defaultVal = None
        matrix =[[defaultVal for _ in range(col)] for _ in range(numRows)]

        # populate matrix
        i = 0
        rowLoc = 0
        colLoc = 0
        direction = -1

        while i < len(s):
            if rowLoc == 0:
                while rowLoc < numRows:
                    if i == len(s):
                        break
                    matrix[rowLoc][colLoc] = s[i]
                    rowLoc += 1
                    i += 1
            
            if rowLoc == numRows:
                rowLoc -= 1
            if rowLoc == numRows - 1:
                while rowLoc != 0:
                    rowLoc -= 1
                    colLoc += 1
                    if rowLoc == 0:
                        break
                    if i == len(s):
                        break
                    matrix[rowLoc][colLoc] = s[i]
                    i += 1
        #printMatrix(matrix)

        convertedStr = ""
        rowLoc = 0
        # covert
        while rowLoc < numRows:
            for item in matrix[rowLoc]:
                if item != None:
                    convertedStr += item
            rowLoc += 1

        return convertedStr


        

def main():
    solution = Solution()
    print(solution.convert("theonepieceisreal", 5))

main()