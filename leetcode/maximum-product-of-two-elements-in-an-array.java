//https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution {
    public int maxProduct(int[] nums) {
        int one = 1;
        int two = 1;
        for(int i = 0; i<nums.length; i++){
            if(nums[i] > one){
                two = one;
                one = nums[i];
            }else if(nums[i] > two){
                two = nums[i];
            }
        }
        return (one-1)*(two-1);
    }
}
