/*
1796. Second Largest Digit in a String
Easy
Topics
premium lock icon
Companies
Hint
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

 

Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and digits.
*/
#include<string>
#include<iostream>
class Solution {
public:
    int secondHighest(std::string s) {
        int highest = -1;
        int secondHighest = -1;
        int currentVal = 0;

        for(int i = 0; i < s.length(); i++){
            currentVal = (int)s[i];
            if(currentVal >= 48 && currentVal <= 57){
                currentVal -= 48;
                if(currentVal > highest){
                    secondHighest = highest;
                    highest = currentVal;
                    continue;
                }
                if(currentVal > secondHighest && currentVal != highest)
                    secondHighest = currentVal;
            }
        }
        return secondHighest;
    }
};

int main(){
    Solution solution = Solution();
    std::cout << solution.secondHighest("a1df1") << std::endl;
    return 0;
}