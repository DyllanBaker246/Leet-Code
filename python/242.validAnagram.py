'''
242. Valid Anagram
Easy
Topics
premium lock icon
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # compare lengths
        if len(s) != len(t):
            return False 
        
        # sort
        sortedS = ''.join(sorted(s))
        sortedT = ''.join(sorted(t))

        #compare
        i = 0
        while i < len(s):
            if sortedS[i] != sortedT[i]:
                return False
            i = i + 1
        return True