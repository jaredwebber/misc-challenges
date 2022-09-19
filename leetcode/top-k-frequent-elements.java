// https://leetcode.com/problems/top-k-frequent-elements/

import java.util.HashMap;
import java.util.PriorityQueue;

class Solution {
    class Pair{
        int freq;
        int val;
        Pair(int f, int v){
            this.freq = f;
            this.val = v;
        }
    }
    
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freq = new HashMap<Integer, Integer>();
        
        for(int i = 0; i<nums.length; i++){
            Integer count = freq.get(nums[i]);
            freq.put(nums[i], count == null ? 1 : count+1);
        }
        
        PriorityQueue<Pair> queue = new PriorityQueue<Pair>((a,b)->b.freq-a.freq);
        
        for(int i: freq.keySet()){
            queue.add(new Pair(freq.get(i), i));
        }
        
        int[] out = new int[k];
        
        for(int i = 0; i<k; i++){
            out[i] = queue.poll().val;
        }
        
        
        return out;
    }
}
