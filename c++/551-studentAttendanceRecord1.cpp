/*
551. Student Attendance Record I
Easy
Topics
premium lock icon
Companies
You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.

 

Example 1:

Input: s = "PPALLP"
Output: true
Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
Example 2:

Input: s = "PPALLL"
Output: false
Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.
 

Constraints:

1 <= s.length <= 1000
s[i] is either 'A', 'L', or 'P'.
*/
#include <string>
#include <iostream>
class Solution {
public:
    bool checkRecord(std::string s) {
        int absentCount = 0;
        int lateCount = 0;
        for(int i = 0; i < s.length(); ++i){
            // std::cout << "absent: " << absentCount << '\n';
            // std::cout << "late: " << lateCount << '\n';
            if(absentCount >= 2)
                return false;
            if(lateCount >= 3)
                return false;
            
            if(s[i] == 'A'){
                absentCount++;
                lateCount = 0;
                continue;
            }

            if(s[i] == 'L'){
                lateCount++;
                continue;
            }
            lateCount = 0;

        }
        if(absentCount >= 2)
            return false;
        if(lateCount >= 3)
            return false;
        return true;
    }
};

int main(){
    Solution solution = Solution();
    bool result = solution.checkRecord("PPALLL");
    std::cout << result << '\n';
    return 0;
}