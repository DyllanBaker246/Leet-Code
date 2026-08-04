'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ref = strs[0]
        current = ""
        i = 1
        length = len(strs)

        # print(i)



        while i < length:
            current = strs[i]
            
            currentLength = len(current)
            refLength = len(ref)
            strLength = 0
            j = 0
            subStr = ""

            strMatch = False

            if currentLength >= refLength:
                strLength = refLength
            else:
                strLength = currentLength
            
            while j < strLength:
                # print(current)
                # print(ref)
                if current[j] == ref[j]:
                    # print(j)
                    # print(current[j])
                    strMatch = True
                    subStr += current[j]
                    # print(subStr)
                    # print(ref)
                    # print(current)
                    # print(subStr)
                    j += 1
                    continue
                strMatch = False
                break
            # print(subStr)
            ref = subStr
            # print(ref)
            if ref == "":
                return "No match"
            
            i += 1

        return ref

    def improvedLongestCommonPrefix(self, strs: list[str]) -> str:
        ref = strs[0]
        i = 1
        length = len(strs)

        while i < length:
            while len(ref) != 0:
                if strs[i].startswith(ref):
                    break
                ref = ref[:-1]
            i += 1
        
        return ref

                    


        
        


def main():
    solution = Solution()
    li = ["flower", "flow", "flight"]
    result = solution.improvedLongestCommonPrefix(li)
    print(result)

main()
