'''
118. Pascal's Triangle
Easy
Topics
premium lock icon
Companies
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
'''
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        tree = [[1]]

        if numRows > 1:
            tree.append([1,1])

        i = 2
        while i < numRows:
            j = 1
            arr = [1]
            while j < len(tree[i-1]):
                arr.append(tree[i-1][j-1] + tree[i-1][j])
                j+=1
            arr.append(1)
            tree.append(arr)
            i += 1
        
        return tree 

def printMatrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            print(matrix[i][j], end = ' ')
            j += 1
        print("")
        i += 1

def main():
    solution = Solution()
    tree = solution.generate(10)

    printMatrix(tree)

main()



