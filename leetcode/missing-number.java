//https://leetcode.com/problems/missing-number/
class Solution {
    public int missingNumber(int[] nums) {
        int sum = 0;
        int expected = nums.length;
        for(int i = 0; i<nums.length; i++){
            expected+=i;
            sum+=nums[i];
        }
        return expected-sum;
    }
}
