//https://leetcode.com/problems/max-consecutive-ones/submissions/

class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max = 0;
        int curr = 0;
        for(int i:nums){
            if(i == 1) curr++;
            else{
                max = max < curr ? curr : max;
                curr = 0;
            }
        }
        return max < curr ? curr : max;
    }
}
