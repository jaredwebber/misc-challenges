//https://leetcode.com/problems/product-of-array-except-self/

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] sums = new int[nums.length];
        
        //find products going 0 through n-1
        int currProd = 1;
        for(int i = 0; i<nums.length; i++){
            sums[i] = currProd;
            currProd*=nums[i];
        }
        
        //include products from n-1 through 0
        currProd = 1;
        for(int i = nums.length-1; i>=0; i--){
            sums[i] *= currProd;
            currProd*=nums[i];
        }
        
        return sums;
    }
}
