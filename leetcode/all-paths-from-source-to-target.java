//https://leetcode.com/problems/all-paths-from-source-to-target/

import java.util.*;

class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> paths = new ArrayList<List<Integer>>();
        
        for(int i:graph[0]){
            ArrayList<Integer> currPath = new ArrayList<Integer>();
            currPath.add(0);
            followPath(paths, graph, i, currPath);
        }
        
        return paths;
    }
    
    private void followPath(List<List<Integer>> paths, int[][] graph, int index, ArrayList<Integer> currPath){
        if(index == graph.length-1){
            currPath.add(index);
            paths.add(currPath);
        }else{
            currPath.add(index);
            ArrayList<Integer> temp = new ArrayList<Integer>(currPath);
            for(int i:graph[index]){
                followPath(paths, graph, i, temp);
                temp = new ArrayList<Integer>(currPath);
            }
        }
    }
}
