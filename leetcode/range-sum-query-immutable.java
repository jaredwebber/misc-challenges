//https://leetcode.com/problems/range-sum-query-immutable/

//DP Sol
class NumArray {
    private int[] sums;
    public NumArray(int[] nums) {
        this.sums = new int[nums.length];
        sums[0] = nums[0];
        for(int i = 1; i<nums.length; i++){
            this.sums[i] = sums[i-1]+nums[i];
        }
    }
    
    public int sumRange(int left, int right) {
        if(left==0) return sums[right];
        return sums[right] - sums[left-1];
    }
}

//Brute Force Sol
/*
class NumArray {
    private int[] nums;
    public NumArray(int[] nums) {
        this.nums = nums;
    }
    
    public int sumRange(int left, int right) {
        int sum = 0;
        for(int i = left; i<=right; i++){
            sum+=this.nums[i];
        }
        return sum;
    }
}
*/
/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */
