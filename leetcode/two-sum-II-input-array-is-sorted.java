//https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
// O(1) Space

// Binary Search When Possible
class Solution {
    public int[] twoSum(int[] numbers, int target) {        
        int lo = 0;
        int mid = numbers.length/2;
        int hi = numbers.length-1;
        
        while(lo < hi){
            if(numbers[lo] + numbers[hi] == target) return new int[]{lo+1,hi+1};
            else if(numbers[lo] + numbers[mid] < target && numbers[mid] + numbers[hi] < target) lo = mid+1;
            else if(numbers[hi] + numbers[mid] > target && numbers[mid] + numbers[lo] > target) hi = mid-1;
            else if(numbers[lo] + numbers[hi] < target){
                lo++;
            }else{
                hi--;
            }
            mid = lo + (hi-lo)/2;
        }
        
        return new int[]{lo+1,hi+1};
    }
}

/* Brute Force
class Solution {
    public int[] twoSum(int[] numbers, int target) {        
        int lo = 0;
        int hi = numbers.length-1;
        
        while(lo < hi){
            if(numbers[lo] + numbers[hi] == target) return new int[]{lo+1,hi+1};
            else if(numbers[lo] + numbers[hi] < target){
                lo++;
            }else{
                hi--;
            }
        }
        
        return new int[]{lo+1,hi+1};
    }
}
*/
