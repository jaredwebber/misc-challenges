//https://leetcode.com/problems/evaluate-division/

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

class Solution {
        
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        double[] ans = new double[queries.size()];
        HashMap<String, HashMap<String, Double>> graph = new HashMap<String, HashMap<String, Double>>();
        
        for(int i = 0; i<equations.size(); i++){
            String one = equations.get(i).get(0);
            String two = equations.get(i).get(1);
            
            graph.putIfAbsent(one, new HashMap<String, Double>());
            graph.get(one).put(two, values[i]);
            graph.putIfAbsent(two, new HashMap<String, Double>());
            graph.get(two).put(one, 1/values[i]);
        }
        
        for(int i = 0; i<queries.size(); i++){            
            ans[i] = findPath(graph, queries.get(i).get(0), queries.get(i).get(1), new HashSet<String>());
        }
        
        return ans;
    }
    
    private double findPath(HashMap<String, HashMap<String, Double>> graph, String source, String dest, HashSet<String> visited){
        visited.add(source);
        if(graph.get(source) != null){
            if(source.equals(dest)) return 1;

            for(String str : graph.get(source).keySet()){
                if(!visited.contains(str)){
                    double val = findPath(graph, str, dest, visited);
                    if(val > 0) return graph.get(source).get(str) * val;
                }
            }
        }
        
        return -1.0;
    }
}
