//https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

class Solution {
    public List<Integer> findLonely(int[] nums) {
        ArrayList<Integer> lonely = new ArrayList<Integer>();
        Arrays.sort(nums);
        if(nums.length >= 2){
            if(nums[1] != nums[0] && nums[1]-1 != nums[0]) lonely.add(nums[0]);
            if(nums[nums.length-2] != nums[nums.length-1] && nums[nums.length-2]+1 != nums[nums.length-1]) lonely.add(nums[nums.length-1]);
            for(int i = 1; i<nums.length-1; i++){
                if(nums[i-1] != nums[i] && nums[i+1] != nums[i] && nums[i-1] + 1 != nums[i] && nums[i+1]-1 != nums[i]) lonely.add(nums[i]);
            }
        }else{
            lonely.add(nums[0]);
        }
        return lonely;
    }
}