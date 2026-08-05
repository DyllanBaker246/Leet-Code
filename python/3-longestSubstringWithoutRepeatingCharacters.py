'''
3. Longest Substring Without Repeating Characters
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 105
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        subStr = ""
        longestLen = 0
        currentLen = 0

        while i < len(s):
            j = i 
            while j < len(s):
                #print(subStr)
                if subStr.find(s[j]) == -1:
                    subStr += s[j]
                    currentLen += 1
                    j += 1
                    if j == len(s):
                        if longestLen < currentLen:
                            longestLen = currentLen
                        return longestLen
                else:
                    if longestLen < currentLen:
                        longestLen = currentLen
                    currentLen = 0
                    subStr = ""
                    break
            i += 1

        if longestLen < currentLen:
            longestLen = currentLen
        return longestLen

                    

def main():
    solution = Solution()
    result = solution.lengthOfLongestSubstring("hello")
    print(result)
main()



    