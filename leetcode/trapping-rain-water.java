//https://leetcode.com/problems/trapping-rain-water/submissions/

class Solution {
    
	// Approach Explanation:
	// https://leetcode.com/problems/trapping-rain-water/discuss/153992/Java-O(n)-time-and-O(1)-space-(with-explanations).
    public int trap(int[] height) {
        int left = 0;
        int right = height.length-1;
        int maxLeft = height[left];
        int maxRight = height[right];
        int sum = 0;
        
        while(left < right){
            // Continue from the lower bar to not overcount
            if(height[left] < height[right]){
                if(height[left] > maxLeft){
                    maxLeft = height[left++];
                }else{
                    sum += maxLeft - height[left++];
                }
            }else{
                if(height[right] > maxRight){
                    maxRight = height[right--];
                }else{
                    sum += maxRight - height[right--];
                }
            }
        }
        
        return sum;
    }
}


