// https://leetcode.com/problems/find-players-with-zero-or-one-losses

import java.util.*;

class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        HashMap<Integer, Integer> losses = new HashMap<Integer, Integer>();
        for(int i = 0; i<matches.length; i++){
            losses.put(matches[i][0], losses.getOrDefault(matches[i][0], 0));
            losses.put(matches[i][1], losses.getOrDefault(matches[i][1], 0)+1);
        }

        List<List<Integer>> list = new ArrayList<List<Integer>>();
        list.add(new ArrayList<Integer>());
        list.add(new ArrayList<Integer>());
        for(int i :losses.keySet()){
            int count = losses.get(i);
            if(count < 2){
                list.get(count).add(i);
            }
        }
        Collections.sort(list.get(0));
        Collections.sort(list.get(1));
        return list;
    }
}
