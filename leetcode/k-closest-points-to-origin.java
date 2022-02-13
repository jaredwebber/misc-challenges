//https://leetcode.com/problems/k-closest-points-to-origin/

import java.util.ArrayList;
import java.util.Collections;

class Solution {
    class Pair implements Comparable<Pair>{
        int[] coords;
        double distance;
        public Pair(int[] coords, double distance){
            this.coords = coords;
            this.distance = distance;
        }
        
        public int compareTo(Pair pair){
            if(this.distance<pair.distance) return -1;
            return 1;
        }
    }
    
    public int[][] kClosest(int[][] points, int k) {
        ArrayList<Pair> distances = new ArrayList<Pair>();
        int[][] closest = new int[k][2];
        
        for(int i = 0; i<points.length; i++){
            int[] temp = new int[] {points[i][0], points[i][1]};
            System.out.println(temp[0]+", "+temp[1]);
            distances.add(new Pair(temp, getDistance(points[i])));
        }
                
        Collections.sort(distances);
                
        for(int i = 0; i<k;i++){
            closest[i][0] = distances.get(i).coords[0];
            closest[i][1] = distances.get(i).coords[1];
        }
        
        return closest;
    }
    
    private double getDistance(int[] coords){
        return Math.sqrt(Math.pow(coords[0],2)+Math.pow(coords[1],2));
    }
}
