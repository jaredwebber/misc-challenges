# https://leetcode.com/problems/letter-combinations-of-a-phone-number


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letter_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if len(digits) == 0:
            return []

        total: int = 1
        for i in digits:
            total *= len(letter_map[i])

        combinations: list[str] = []
        for d in letter_map[digits[0]]:
            for i in range(int(total / len(letter_map[digits[0]]))):
                combinations.append(d)

        index: int = 0
        for i in range(1, len(digits)):
            index = 0
            if i > 1:
                combinations.sort()
            for _ in range(int(total / len(letter_map[digits[i]]))):
                for d in letter_map[digits[i]]:
                    combinations[index] += d
                    index += 1

        return combinations
