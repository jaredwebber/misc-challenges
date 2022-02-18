//https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

import java.util.Arrays;

class Solution {
    public int minimumSum(int num) {
        int[] digits = new int[4];
        for(int i = 0; i<4; i++){
            digits[i] = Integer.parseInt(String.valueOf((""+num).charAt(i)));
        }
        Arrays.sort(digits);

        return digits[0]*10+digits[2] + digits[1]*10 +digits[3];
    }
}