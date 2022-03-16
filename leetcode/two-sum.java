//https://leetcode.com/problems/two-sum/

import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] values = new int[2];
        HashMap<Integer, Integer> mapping = new HashMap<Integer, Integer>(); 
        for(int i = 0; i<nums.length; i++){
            if(mapping.containsKey(target - nums[i])){
                values[0] = mapping.get(target - nums[i]);
                values[1] = i;
                break;
            }
            mapping.put(nums[i], i);
        }
        return values;
    }
}

/* Unoptimized:
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        for(int i = 0;i<nums.length; i++){
            for(int j=i+1; j<nums.length; j++){
                if(nums[i]+nums[j] == target){
                    result[0] = i;
                    result[1] = j;
                    return result;
                }
            }
        }
        return null;
    }
}
*/