/*
1005. Maximize Sum Of Array After K Negations
Easy
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, modify the array in the following way:

choose an index i and replace nums[i] with -nums[i].
You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.

 

Example 1:

Input: nums = [4,2,3], k = 1
Output: 5
Explanation: Choose index 1 and nums becomes [4,-2,3].
Example 2:

Input: nums = [3,-1,0,2], k = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
Example 3:

Input: nums = [2,-3,-1,5,-4], k = 2
Output: 13
Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
 

Constraints:

1 <= nums.length <= 104
-100 <= nums[i] <= 100
1 <= k <= 104
*/  
#include<iostream>
#include<vector>
#include<algorithm>
class Solution {
public:
    int largestSumAfterKNegations(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());

        int count = k;
        int i = 0;
        int sum = 0;
        
        while(i < nums.size() && count != 0 && nums[i] < 0){
            nums[i] = nums[i] * -1;
            count--;
            i++;
            std::cout << nums[i] << std::endl;
        }
        // after making negatives positive
        

        std::sort(nums.begin(), nums.end());

        if(count > 0){
            if(count % 2 == 1)
                nums[0] = nums[0] * -1;
                std::cout << nums[0] << std::endl;
        }

        for(int j = 0; j < nums.size(); j++){
            sum += nums[j];
        }

        return sum;
    }
};

int main(){
    Solution solution = Solution();
    std::vector<int> vec = {-2,5,0,2,-2};
    std::cout << solution.largestSumAfterKNegations(vec, 3) << std::endl;
    return 0;
}