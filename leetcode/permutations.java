//https://leetcode.com/problems/permutations/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> permute(int[] nums) {       
        return search(new ArrayList<List<Integer>>(), new ArrayList<Integer>(), nums);
    }
    
    private List<List<Integer>> search(List<List<Integer>> permutations, List<Integer> curr, int[] nums){
        if(curr.size() == nums.length){
            permutations.add(curr);
        }else{
            for(int i:nums){
                if(!curr.contains(i)){
                    ArrayList<Integer> next = new ArrayList<Integer>();
                    next.addAll(curr);
                    next.add(i);
                    search(permutations, next, nums);
                }
            }
        }
        return permutations;
    }
}