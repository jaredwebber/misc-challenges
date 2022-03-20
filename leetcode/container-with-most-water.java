//https://leetcode.com/problems/container-with-most-water/

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
