//https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution {
    public int longestOnes(int[] nums, int k) {
        int max = 0;
        int left = 0;
        int right = 0;
        int flipped = 0;
        
        while(right < nums.length){
            if(nums[right] == 0){
                if(flipped < k) flipped ++;
                else while(nums[left++] != 0){}
            }
            max = Math.max((right-left)+1, max);
            right++;
        }
        
        return max;
    }
}
