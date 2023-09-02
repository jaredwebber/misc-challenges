# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left_side: int = n - index - 1  # positions left of index
        right_side: int = index  # positions right of index
        low: int = 0
        hi: int = maxSum
        mid: int
        ans: int = 1

        curr_sum: int
        left_sum: int
        right_sum: int
        mmo: int  # mid minus 1

        while low <= hi:
            mid = (low + hi) // 2
            curr_sum = mid
            left_sum = 0
            right_sum = 0
            mmo = mid - 1

            if left_side <= mid - 1:
                # sum of (mid-left_side) to mmo
                right_sum = ((mmo * mid) // 2) - (mmo - left_side) * (
                    mid - left_side
                ) // 2
            else:
                # sum of 1 to mmo plus 1 for each remaining index
                right_sum = mmo * mid // 2 + left_side - mmo

            if right_side <= mid - 1:
                # sum of (mid-right_side) to mmo
                left_sum = mmo * mid // 2 - (mmo - right_side) * (mid - right_side) // 2
            else:
                # sum of 1 to mmo plus 1 for each remaining index
                left_sum = (mmo * mid // 2) + (right_side - mmo)

            curr_sum += left_sum + right_sum

            if curr_sum <= maxSum:
                ans = mid
                low = mid + 1
            else:
                hi = mid - 1
        return ans
