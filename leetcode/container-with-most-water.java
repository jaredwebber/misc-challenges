//https://leetcode.com/problems/container-with-most-water/

//Slightly Optimized Syntax
class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0;
        int left = 0;
        int right = height.length-1;
        
        while(left < right){
            // Equivalent to Math.max(maxArea, (right-left) * Math.min(height[left], height[right]))
            maxArea = maxArea < (height[left] < height[right] ? height[left] : height[right])*(right-left) ? (height[left] < height[right] ? height[left] : height[right])*(right-left) : maxArea;
            if(height[left]<height[right]) left++;
            else right--;
        }
        
        return maxArea;
    }
}

/* Clean to read solution
class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0;
        int left = 0;
        int right = height.length-1;
        int currArea = 0;
        
        while(left<right){
            if(height[left] < height[right]){
                currArea = (right-left) * height[left];
                left++;
            }else{
                currArea = (right-left) * height[right];
                right--;
            }
            maxArea = Math.max(currArea, maxArea);
        }
        
        return maxArea;
    }
}
*/
