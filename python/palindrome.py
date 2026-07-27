class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        current = 0
        nums = []
        count = 0
        remainder = x

        print(nums)

        while remainder > 0:
            current = remainder % 10
            remainder = remainder // 10
            nums.append(current)

            print(current)

        print(nums)

        reverseIndex = len(nums) - 1
        for num in nums:
            print(num)
            if num != nums[reverseIndex]:
                return False
            reverseIndex -= 1

        return True

def main():
    solution = Solution()

    result = solution.isPalindrome(-121)

    print(result)

main()
