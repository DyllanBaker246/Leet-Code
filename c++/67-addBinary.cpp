/*
67. Add Binary
Easy
Topics
premium lock icon
Companies
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
*/
#include<string>
#include <iostream>
class Solution {
public:
    std::string betterAddBinary(std::string a, std::string b){
        bool carry = false;
        std::string res = "";
        std::string str1 = a;
        std::string str2 = b;
        int len1 = str1.length();
        int len2 = str2.length();
        int diff = abs(len1 - len2);

        if(len1 > len2){
            str2.insert(0, diff,'0');
        }
        if(len1 < len2){
            str1.insert(0,diff,'0');
        }

        // once lengths are ==
        for(int i = str1.length() -1; i >= 0; i--){
            std::cout << res << std::endl;
            // 1 + 1 + 0
            if(str1[i] == '1' && str2[i] == '1' && !carry){
                res.insert(0,1,'0');
                carry = true;
                continue;
            }
            // 1 + 1 + 1
            if(str1[i] == '1' && str2[i] == '1' && carry){
                res.insert(0,1,'1');
                carry = true;
                continue;
            }
            // 1 + 0 + 1
            if(str1[i] != str2[i] && carry){
                res.insert(0,1,'0');
                carry = true;
                continue;
            }
            // 1 + 0 + 0
            if(str1[i] != str2[i] && !carry){
                res.insert(0,1,'1');
                carry = false;
                continue;
            }
            if(carry){
                res.insert(0,1,'1');
                carry = false;
                continue;
            }else{
                res.insert(0,1,'0');
                carry = false;
                continue;
            }
        }
        if(carry)
            res.insert(0,1,'1');
        return res;
    }

    std::string addBinary(std::string a, std::string b) {
        int val1 = binaryToInt(a);
        int val2 = binaryToInt(b);

        int total = val1 + val2;
        if(total == 0)
            return "0";
        return intToBinary(total);
    }

    int binaryToInt(std::string s){
        int current = 1;
        int total = 0;
        for (int i = s.length() -1; i >= 0; i--){
            if(s[i] == '1'){
                total += current;
            }
            current *= 2; // leads to int overflow
        }

        return total;
    }

    std::string intToBinary(int num){
        std::string res = "";
        int remainder = num;
        //std::cout << remainder;
        while(remainder != 0){
            //std::cout << remainder << std::endl;
            char c = '0' + (remainder % 2);
            // std::cout << c << std::endl;
            // std::cout << c << std::endl;
            res.insert(0, 1, c);
            // std::cout << res << std::endl;
            remainder /= 2;
        }

        return res;
    }
};

int main(){
    Solution solution = Solution();
    std::string res = solution.betterAddBinary("1010", "1011");
    std::cout << res << std::endl;
    return 0;
}