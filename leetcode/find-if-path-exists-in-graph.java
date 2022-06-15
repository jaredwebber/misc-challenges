//https://leetcode.com/problems/find-if-path-exists-in-graph/

import java.util.HashSet;

class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        HashSet<Integer> accessible = new HashSet<Integer>();
        accessible.add(source);
        
        for(int i = 0; i<edges.length; i++){
            if(accessible.contains(edges[i][0]) || accessible.contains(edges[i][1])){
                accessible.add(edges[i][0]);
                accessible.add(edges[i][1]);
            }
        }
        
        for(int i = 0; i<edges.length && accessible.size() < n; i++){
            if(accessible.contains(edges[i][0]) || accessible.contains(edges[i][1])){
                accessible.add(edges[i][0]);
                accessible.add(edges[i][1]);
            }
        }
        
        return accessible.contains(destination);
    }
}
