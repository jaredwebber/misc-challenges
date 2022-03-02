//https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution {
    public int[] decompressRLElist(int[] nums) {
        int[] freq = new int[nums.length/2];
        int[] vals = new int[nums.length/2];
        int[] answer = null;
        int size = 0;
        
        for(int i = 0; i<nums.length; i+=2){
            freq[i/2] = nums[i];
            vals[i/2] = nums[i+1];
            size += freq[i/2];
        }
                
        int index=0;
        answer = new int[size];
        for(int i = 0; i<freq.length; i++){
            for(int j = 0; j<freq[i]; j++){
                answer[index++] = vals[i];
            }
        }
        return answer;
    }
}
