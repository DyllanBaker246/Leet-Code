/*
191. Number of 1 Bits
Easy
Topics
premium lock icon
Companies
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

 

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 

Constraints:

1 <= n <= 231 - 1
*/
#include<string>
#include<iostream>
class Solution {
public:
    int hammingWeight(int n) {
        std::string str = intToBin(n);
        int count = 0;

        for (int i = 0; i < str.length(); i++){
            if(str[i] == '1')
                count++;
        }
        return count;
    }

    std::string intToBin(int n){
        if(n == 0)
            return "0";
        int current = n;
        std::string str = "";
        while(current != 0){
            if(current % 2 == 0)
                str.insert(0, 1, '0');
            else
                str.insert(0, 1, '1');
            current /= 2;
        }

        return str;
    }
};

int main(){
    Solution solution = Solution();
    std::cout << solution.intToBin(10) << std::endl;
    std::cout << solution.hammingWeight(10) << std::endl;
    return 0;
}