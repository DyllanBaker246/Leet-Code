'''
13. Roman to Integer - Easy
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. The same principle applies to the number nine, 
which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].


M C M X C I V
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        length = len(s)
        revStr = "".join(reversed(s))
        total = 0
        current = 0
        current = revStr[0]
        count = 1
        subTotal = 0
        
        if revStr[0] == 'I':
            currentInt = 1
        if revStr[0] == 'V':
            currentInt = 5
        if revStr[0] == 'X':
            currentInt = 10
        if revStr[0] == 'L':
            currentInt = 50
        if revStr[0] == 'C':
            currentInt = 100
        if revStr[0] == 'D':
            currentInt = 500
        if revStr[0] == 'M':
            currentInt = 1000

        total = currentInt

        while count < length:
            if revStr[count] == 'I':
                nextInt = 1
            if revStr[count] == 'V':
                nextInt = 5
            if revStr[count] == 'X':
                nextInt = 10
            if revStr[count] == 'L':
                nextInt = 50
            if revStr[count] == 'C':
                nextInt = 100
            if revStr[count] == 'D':
                nextInt = 500
            if revStr[count] == 'M':
                nextInt = 1000

            
            if currentInt > nextInt:
                total -= nextInt
            else:
                total += nextInt

            count += 1

        return total
        
            


def main():
    solution = Solution()
    result = solution.romanToInt("MCMXCIV")
    print(result)

main()