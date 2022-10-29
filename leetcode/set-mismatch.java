// https://leetcode.com/problems/set-mismatch/

import java.util.Arrays;

class Solution {
    public int[] findErrorNums(int[] nums) {
        int[] out = new int[2];
        Arrays.sort(nums);
        int last = nums[0];
        if(last != 1) out[1] = 1;
        
        for(int i = 1;i<nums.length; i++){
            if(nums[i] > last+1) out[1] = nums[i]-1;
            else if(nums[i] == last) out[0] = nums[i];
            last = nums[i];
        }
        if(out[1] == 0) out[1] = nums.length;
        return out;
    }
}
