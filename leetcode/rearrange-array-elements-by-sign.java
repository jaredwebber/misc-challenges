

//temp
class Solution {
    public int[] rearrangeArray(int[] nums) {
        for(int i = 1; i<nums.length-1; i++){
            if(nums[i-1]>=0 && nums[i]>=0) nums = swap(i, nums);
            if(nums[i-1]<0 && nums[i]<0) nums = swap(i, nums);
        }
        return nums;
    }
    
    private int[] swap(int index, int[] arr){
        int a = arr[index];
        arr[index] = arr[index+1];
        arr[index+1] = a;
        return arr;
    }
}

//time limit exceeded
class Solution {
    public int[] rearrangeArray(int[] nums) {
        ArrayList<Integer> neg = new ArrayList<Integer>(nums.length/2);
        ArrayList<Integer> pos = new ArrayList<Integer>(nums.length/2);
        for(int i:nums){
            if(i < 0) neg.add(i);
            else pos.add(i);
        }
        
        for(int i = 0; i<nums.length-1; i+=2){
            nums[i] = pos.remove(0);
            nums[i+1] = neg.remove(0);
        }
        
        return nums;
    }
}