// https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

import java.util.HashSet;
import java.util.PriorityQueue;

class Solution {
    public int[] maxSubsequence(int[] nums, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>((i,j)->Integer.compare(i[0],j[0]));
        HashSet<Integer> indices = new HashSet<Integer>();
        int[] out = new int[k];
        
        for(int i = 0; i<nums.length; i++){
            pq.offer(new int[]{nums[i], i});
            if(pq.size() > k) pq.poll();
        }
        
        while(!pq.isEmpty()){
            indices.add(pq.poll()[1]);
        }
        
        int index = 0;
        for(int i = 0; i<nums.length && index < k; i++){
            if(indices.contains(i)) out[index++] = nums[i];
        }
        
        return out;
    }
}