/*
258. Add Digits
Easy
Topics
premium lock icon
Companies
Hint
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1
*/
#include <iostream>
class Solution {
public:
    int addDigits(int num) {
        int remainder = num;
        int total = 0;
        int result = num;
        while(result >= 10){
            // std::cout << "result: " << result << '\n';
            while(remainder > 0){
                total += remainder % 10;
                remainder /= 10;
            }
            result = total;
            remainder = total;
            total = 0;
        }

        return result;
    }
};

int main(){
    Solution solution = Solution();
    std::cout << solution.addDigits(19) << '\n';
    return 0;
}