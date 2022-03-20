//https://leetcode.com/problems/jump-game/

class Solution {
    public boolean canJump(int[] nums) {
        int canReach = 0;
        for(int i = 0; i<nums.length && canReach < nums.length-1; i++){
            if(i > canReach) return false;
            canReach = i+nums[i] > canReach ? i+nums[i] : canReach;
        }
        return true;
    }
}

/* Time Limit Exceeded: Recursive Approach
class Solution {
    public boolean canJump(int[] nums) {
        return jump(nums, 0);
    }
    
    private boolean jump(int[] nums, int index){
        if(index == nums.length-1) return true;
        if(index > nums.length-1 || nums[index] == 0) return false;
        
        boolean canJump = false;
        for(int i = 1; i<=nums[index]; i++){
            canJump = canJump || jump(nums, index+i);
        }
        return canJump;
    }
}
*/
