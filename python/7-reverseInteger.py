'''
7. Reverse Integer
Medium
Topics
premium lock icon
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''
import sys

class Solution:
    def reverse(self, x: int) -> int:

        revInt = 0
        num = x
        isNegative = False

        if num < 0:
            num *= -1
            isNegative = True

        while num != 0:
            revInt *= 10
            current = num % 10
            num = num // 10

            revInt += current

        if isNegative:
            revInt *= -1
        if revInt <= -2**31 or revInt > 2**31 - 1:
            return 0
        return revInt

def main():
    solution = Solution()
    print(solution.reverse(1563847412))
main()
            
