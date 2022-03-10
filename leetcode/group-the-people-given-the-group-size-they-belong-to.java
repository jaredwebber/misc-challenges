//https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        HashMap<Integer, ArrayList<Integer>> mapCount = new HashMap<Integer, ArrayList<Integer>>();
        
        for(int i = 0; i<groupSizes.length; i++){
            ArrayList<Integer> indices = mapCount.remove(groupSizes[i]);
            if(indices == null) indices = new ArrayList<Integer>();
            indices.add(i);
            mapCount.put(groupSizes[i], indices);    
        }
        
        List<List<Integer>> output = new ArrayList<List<Integer>>();
        for(int i:mapCount.keySet()){
            ArrayList<Integer> indices = mapCount.get(i);
            int index = 0;
            for(int j = 0; j<indices.size()/i; j++){
                ArrayList<Integer> group = new ArrayList<Integer>();
                while(index<(j+1)*i){
                    group.add(indices.get(index));
                    index++;
                }
                output.add(group);
            }
        }
        
        return output;
    }
}
