'''
11. Container With Most Water
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104   
'''
class Solution:
    def maxArea(self, height: list[int]) -> int: # works but runs O(n**2)
        biggestArea = 0 
        i = 0

        if len(height) == 1:
            return height[0]

        while i < (len(height) - 1):
            j = i + 1
            if height[i] * (len(height) - i + 1) < biggestArea:
                i += 1
                continue
            while j < len(height):
                
                if height[i] > height[j]:
                    shortestHeight = height[j]
                else:
                    shortestHeight = height[i]
                # print("Biggest Area:", end ='')
                # print(biggestArea)
                # print("shortest height:", end='')
                # print(shortestHeight)

                if shortestHeight * (j - i) > biggestArea:
                    biggestArea = shortestHeight * (j - i)
                j += 1
            i += 1
        return biggestArea

    def betterMaxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        biggestArea = 0

        if len(height) == 1:
            return height[0]

        while left < right:
            width = right - left
            if height[left] < height[right]:
                shortestHeight = height[left]
            else:
                shortestHeight = height[right]
            
            if shortestHeight * width > biggestArea:
                biggestArea = shortestHeight * width

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return biggestArea


def main():
    solution = Solution()
    print(solution.betterMaxArea([1]))
main()