# https://leetcode.com/problems/integer-to-english-words


class Solution:
    digit_strings: dict[str, str] = {
        "0": "Zero",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "10": "Ten",
        "11": "Eleven",
        "12": "Twelve",
        "13": "Thirteen",
        "14": "Fourteen",
        "15": "Fifteen",
        "16": "Sixteen",
        "17": "Seventeen",
        "18": "Eighteen",
        "19": "Nineteen",
        "20": "Twenty",
    }

    tens_strings: dict[str, str] = {
        "2": "Twenty",
        "3": "Thirty",
        "4": "Forty",
        "5": "Fifty",
        "6": "Sixty",
        "7": "Seventy",
        "8": "Eighty",
        "9": "Ninety",
    }

    quantifier_strings: dict[str, str] = {1: "Thousand", 2: "Million", 3: "Billion"}

    def numberToWords(self, num: int) -> str:
        num_str: str = str(num)
        words: str = ""
        end_index: int = len(num_str)
        start_index: int = end_index - 3
        quant_index: int = 0

        while start_index >= 0:
            section: str = self.three_digit_block_string(num_str[start_index:end_index])
            words = (
                section
                + (
                    " " + self.quantifier_strings[quant_index] + " "
                    if quant_index > 0 and len(section) > 0
                    else ""
                )
                + words
            )
            start_index -= 3
            end_index -= 3
            quant_index += 1

        remainder: str = self.two_digit_block_string(num_str[0:end_index])

        return (
            remainder
            + (
                " " + self.quantifier_strings[quant_index] + " "
                if quant_index > 0 and len(remainder) > 0
                else ""
            )
            + words
        ).strip()

    def three_digit_block_string(self, block: str) -> str:
        if len(block) == 0:
            return ""

        block_num: int = int(block)

        if len(block) < 3:
            return self.two_digit_block_string(block)

        if block_num == 0:
            return ""

        return (
            self.digit_strings[block[0]] + " Hundred" if block[0] != "0" else ""
        ) + (
            (" " if block[0] != "0" else "") + self.two_digit_block_string(block[1:])
            if block[1:] != "00"
            else ""
        )

    def two_digit_block_string(self, block: str) -> str:
        if len(block) == 0:
            return ""

        block_num: int = int(block)

        if block_num <= 20:
            return self.digit_strings[str(block_num)]

        return self.tens_strings[block[0]] + (
            (" " + self.digit_strings[block[1]])
            if (self.digit_strings.get(block[1]) and block[1] != "0")
            else ""
        )
