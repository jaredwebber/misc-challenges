# https://leetcode.com/problems/gas-station


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # if impossible, return -1
        if sum(gas) < sum(cost):
            return -1

        # knowing its possible...
        index: int = 0
        tank: int = 0

        for i in range(len(gas) - 1):
            tank += gas[i] - cost[i]
            if tank < 0:
                index = i + 1
                tank = 0

        return index
