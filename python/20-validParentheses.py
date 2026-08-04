'''
20. Valid Parentheses
Easy
Topics
premium lock icon
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        charList = list(s)
        stack = []
        currentChar = ""

        for item in s:
            if item == "[" or item == "(" or item == "{":
                stack.append(item)
                continue

            if not stack:
                return False
            currentChar = stack.pop()
            print(currentChar)
            if currentChar != "(" and item == ")":
                return False
            if currentChar != "[" and item == "]":
                return False
            if currentChar != "{" and item == "}":
                return False
        
        if stack:
            return False
        return True

def main():
    solution = Solution()
    print(solution.isValid("((("))

main()