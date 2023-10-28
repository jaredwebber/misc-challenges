# https://leetcode.com/problems/student-attendance-record-i


class Solution:
    def checkRecord(self, s: str) -> bool:
        late: int = 0
        absent: int = 0
        for i in s:
            if i == "L":
                late += 1
                if late == 3:
                    return False
            else:
                if i == "A":
                    absent += 1
                    if absent == 2:
                        return False
                late = 0
        return True
