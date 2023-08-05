# https://leetcode.com/problems/expressive-words


class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        count_letter_in_order: list[tuple(str, int)] = []
        count_expressive: int = 0

        count: int = 0
        last: str = ""
        for i in s:
            if last == "" or i == last:
                count += 1
            else:
                count_letter_in_order.append((last, count))
                count = 1
            last = i
        count_letter_in_order.append((last, count))

        index: int = 0
        word_sections: int = 0
        for w in words:
            last = ""
            count = 0
            index = 0
            word_sections = 1
            for i in w:
                if index == -1:
                    continue
                if last == "" or i == last:
                    count += 1
                else:
                    if count > count_letter_in_order[index][1] or (
                        count_letter_in_order[index][1] < 3 and count != count_letter_in_order[index][1]
                    ):
                        index = -1
                    index += 1
                    count = 1
                    word_sections += 1
                    if index >= len(count_letter_in_order) or count_letter_in_order[index][0] != i:
                        index = -1
                last = i
            if (
                count > count_letter_in_order[index][1]
                or (count_letter_in_order[index][1] < 3 and count != count_letter_in_order[index][1])
                or count_letter_in_order[index][0] != i
                or word_sections != len(count_letter_in_order)
            ):
                index = -1
            if index != -1:
                count_expressive += 1

        return count_expressive
