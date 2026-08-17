'''
520. Detect Capital
Easy
Topics
premium lock icon
Companies
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
 

Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        
        firstChar = ord(word[0])
        print(firstChar)

        # First char is a lowercase
        if firstChar >= 97:
            i = 1
            while i < len(word):
                if ord(word[i]) < 97:
                    return False
                i += 1
            return True
        
        # First char is cap
        secondChar = ord(word[1])
        print(secondChar)

        #------Second char is lowercase
        if secondChar >= 97:
            i = 2
            while i < len(word):
                if ord(word[i]) < 97:
                    return False
                i += 1
            return True
        #-------Second char is cap
        i = 2
        while i < len(word):
            if ord(word[i]) >= 97:
                return False
            i += 1
        return True

def main():
    solution = Solution()
    print(solution.detectCapitalUse("USA"))
main()