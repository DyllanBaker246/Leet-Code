'''
4. Median of Two Sorted Arrays
Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''
import math
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        sortedList = sorted(nums1 + nums2)
        length = len(sortedList)

        if length % 2 == 0:
            half = length // 2
            median = (sortedList[half] + sortedList[half - 1]) / 2
            return median
        half = length / 2
        median = sortedList[math.floor(half)]
        return median
        

        
        
def printList(nums: list[int]):
    for item in nums:
        print(item)

def main():
    solution = Solution()
    nums1 = [1,3]
    nums2 = [2]
    nums = solution.findMedianSortedArrays(nums1,nums2)
    print(nums)
    
main()