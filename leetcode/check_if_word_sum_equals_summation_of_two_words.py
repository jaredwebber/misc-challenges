# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first_sum: str = ""
        second_sum: str = ""
        target_sum: str = ""

        for i in firstWord:
            first_sum += str(ord(i) - 97)

        for i in secondWord:
            second_sum += str(ord(i) - 97)

        for i in targetWord:
            target_sum += str(ord(i) - 97)

        return int(first_sum) + int(second_sum) == int(target_sum)
