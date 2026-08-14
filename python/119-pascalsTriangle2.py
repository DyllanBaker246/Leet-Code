'''
119. Pascal's Triangle II
Easy
Topics
premium lock icon
Companies
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
'''
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        prev = [1]
        if rowIndex == 0:
            return prev
        current = [1,1]
        if rowIndex == 1:
            return current
        
        prev = [1,1]
        current = [1]
        i = 2
        while i <= rowIndex:
            j = 0
            current = [1]
            while j < len(prev) - 1:
                current.append(prev[j] + prev[j + 1])
                j += 1
            current.append(1)
            prev = current
            i += 1

        return prev

def main():
    solution = Solution()
    arr = solution.getRow(4)
    for item in arr:
        print(item, end=' ')

main()
            
