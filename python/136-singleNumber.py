'''
136. Single Number
Easy
Topics
premium lock icon
Companies
Hint
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return nums[0]
        
        arr = sorted(nums)
        if arr[0] != arr[1]:
            return arr[0]
        if arr[len(arr) - 1] != arr[len(arr) - 2]:
            return arr[len(arr) - 1]

        i = 1

        while i < len(arr) - 1:
            if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
                return arr[i]
            i += 1
        return -1

def main():
    solution = Solution()
    print(solution.singleNumber([1,2]))

main()