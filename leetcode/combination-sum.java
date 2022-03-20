//https://leetcode.com/problems/combination-sum/submissions/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> combinations = new ArrayList<>();
        if(candidates.length == 0) return combinations;
        
        Arrays.sort(candidates);
        recursiveCombinations(combinations, new ArrayList<Integer>(), candidates, target, 0);
        
        return combinations;
    }
    
    private void recursiveCombinations(List<List<Integer>> combinations, List<Integer> curr, int[] candidates, int target, int startIndex){
        if(target == 0) combinations.add(new ArrayList<Integer>(curr));
        else if(target>0){
            for(int i = startIndex; i<candidates.length; i++){
                curr.add(candidates[i]);
                recursiveCombinations(combinations, curr, candidates, target-candidates[i], i);
                curr.remove(curr.size()-1);
            }
        }
    }
}
