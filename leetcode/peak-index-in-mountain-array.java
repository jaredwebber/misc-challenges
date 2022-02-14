//https://leetcode.com/problems/peak-index-in-a-mountain-array/

//More Efficient Solution
class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        for(int i = 0; i<arr.length; i++){
            if(arr[i]>arr[i+1]) return i;
        }
        return 0;
    }
}

//Less Efficient
/*
class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int maxPeakValue = 0;
        int maxPeakIndex = 0;
        for(int i = 1; i<arr.length-1; i++){
            if(arr[i]>arr[i-1] && arr[i]>arr[i+1] && arr[i]>maxPeakValue){
                maxPeakValue = arr[i];
                maxPeakIndex = i;
            }
        }
        return maxPeakIndex;
    }
}
*/