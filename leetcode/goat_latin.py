# https://leetcode.com/problems/goat-latin


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels: list[str] = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
        goat: str = ""
        sentence_arr: list[str] = sentence.split()

        for i in range(len(sentence_arr)):
            if i != 0:
                goat += " "
            if sentence_arr[i][0] in vowels:
                goat += sentence_arr[i]
            else:
                goat += sentence_arr[i][1:] + sentence_arr[i][0]
            goat += "ma" + (i + 1) * "a"
        return goat
