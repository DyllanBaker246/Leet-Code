/*
217. Contains Duplicate
Easy
Topics
premium lock icon
Companies
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true
*/
#include<algorithm>
#include<iostream>
#include<vector>

class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        std::vector<int> sortedNums = nums;
        std::sort(sortedNums.begin(), sortedNums.end());
        int current = sortedNums[0];

        for(int i = 1; i < sortedNums.size(); i++){
            if(current == sortedNums[i])
                return true;
            current = sortedNums[i];
        }

        return false;
    }
};

