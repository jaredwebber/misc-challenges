//https://leetcode.com/problems/3sum/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> sums = new ArrayList<>();
        int left = 0;
        int right = 0;
        int currSum = 0;
        
        if(nums.length < 3) return sums;
        
        Arrays.sort(nums);
        
        for(int i = 0; i<nums.length-2; i++){
            if(nums[i] > 0) break;
            
            if(i == 0 || nums[i] != nums[i-1]){
                left = i+1;
                right = nums.length-1;
                while(left<right){
                    currSum = nums[i] + nums[left] + nums[right];
                    if(currSum == 0){
                        sums.add(Arrays.asList(nums[i], nums[left], nums[right]));
                        while(left<right && nums[left] == nums[left+1]) left++;
                        while(left<right && nums[right] == nums[right-1]) right--;
                        left++;
                        right--;
                    }else if(currSum < 0){
                        left++;
                    }else{
                        right--;
                    }
                }
            }
        }
        
        return sums;
    }
}