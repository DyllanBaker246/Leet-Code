'''
5. Longest Palindromic Substring
Medium

Hint
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''
import math
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        currentPal = s[0]
        currentPalLen = 1
        i = 0
        while i < len(s):
            print("i =",i)
            j = i
            while j < len(s):
                print("j =",j)
                substring = s[i:j+1]
                print(substring)
                print("=============================")
                
                if self.isPalindrome(substring):
                    if len(substring) == 1:
                        j=j+currentPalLen
                        continue
                    if len(currentPal) > len(substring):
                        j=j+currentPalLen
                        continue
                    currentPal = substring
                j = j+currentPalLen
            i = i+1
        return currentPal
                

        return ""
    def betterIsPalindrome(self, s:str) -> bool:
        if len(s) == 1:
            return True
        mid = len(s)
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        first = 0
        last = len(s) - 1

        while last > first:
            if s[first] is not s[last]:
                return False
            first = first + 1
            last = last - 1
        return True
def main():
    solution = Solution()
    print(solution.longestPalindrome("ccc"))

main()
