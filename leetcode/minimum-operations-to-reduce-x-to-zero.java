//https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

// Problem Approach: Find the shortest subarray with sum = arraySum - x
class Solution {
    public int minOperations(int[] nums, int x) {
        int sum = 0;
        int curr = 0;
        int left = 0;
        int right = 0;
        int minLength = -1;
        
        for(int i:nums) sum+=i;
        
        sum-=x;
        
         while(right < nums.length){
            curr+=nums[right];
            if(curr > sum){
                while(curr > sum && left <= right){
                    curr-=nums[left++];
                }
            }

            if(curr == sum){
                minLength = Math.max(minLength,right-left+1);
            }
            right++;
        }
        
        return minLength != -1 ? nums.length - minLength : -1;
    }    
}