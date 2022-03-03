//https://leetcode.com/problems/find-center-of-star-graph/

class Solution {
    public int findCenter(int[][] edges) {
        return edges[0][0] == edges[1][0] || edges[0][0] == edges[1][1] ? edges[0][0] : edges[0][1];
    }
}

/* Brute Force Strategy

import java.util.HashMap;

class Solution {
    public int findCenter(int[][] edges) {
        HashMap<Integer, Integer> pointEdges = new HashMap<Integer, Integer>();
        for(int i = 0; i<edges.length; i++){
            int curr = 0;
            if(pointEdges.get(edges[i][0]) == null) pointEdges.put(edges[i][0], 1);
            else{
                curr = pointEdges.get(edges[i][0]);
                if(curr==edges.length-1) return edges[i][0];
                else pointEdges.put(edges[i][0], curr+1);
            }
            if(pointEdges.get(edges[i][1]) == null) pointEdges.put(edges[i][1], 1);
            else{
                curr = pointEdges.get(edges[i][1]);
                if(curr==edges.length-1) return edges[i][1];
                else pointEdges.put(edges[i][1], curr+1);
            }
        }
        return 0;
    }
}
*/
