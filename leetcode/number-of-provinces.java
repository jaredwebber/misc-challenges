//https://leetcode.com/problems/number-of-provinces/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

// Inefficient Solution runtime & space
class Solution {
    public int findCircleNum(int[][] isConnected) {
        ArrayList<ArrayList<Integer>> provinces = new ArrayList<ArrayList<Integer>>();
        
        for(int i = 0; i<isConnected.length; i++){
            find(isConnected, provinces, i, new ArrayList<Integer>());
        }
                
        HashSet<String> unique = new HashSet<String>();
        for(ArrayList<Integer> i: provinces){
            unique.add(i.toString());
        }
        
        return unique.size();
    }
    
    private void find(int[][] isConnected, ArrayList<ArrayList<Integer>> connections, int index, ArrayList<Integer> currSet){ 
        if(!currSet.contains(index)) currSet.add(index);
        for(int i = 0; i<isConnected.length; i++){
            if(!currSet.contains(i) && isConnected[index][i] == 1) find(isConnected, connections, i, currSet);
        }
        Collections.sort(currSet);
        if(!connections.contains(currSet)) connections.add(currSet);
    }
}
