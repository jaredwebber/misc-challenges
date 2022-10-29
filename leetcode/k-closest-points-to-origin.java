//https://leetcode.com/problems/k-closest-points-to-origin/

import java.util.PriorityQueue;

class Solution {
    class Pair implements Comparable{
        double dist;
        int[] point;
        Pair(int[] point, double dist){
            this.point = point;
            this.dist = dist;
        }
        
        public int compareTo(Object o){
            if(o instanceof Pair){
                return ((Pair)o).dist < this.dist ? 1 : -1;
            }
            return -1;
        }
    }

    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Pair> queue = new PriorityQueue<Pair>();
        int[][] output = new int[k][2];
            
        for(int[] i: points){
            queue.add(new Pair(i, Math.sqrt(Math.pow(i[0], 2) + Math.pow(i[1], 2))));
        }
        
        while(k>0){
            output[k---1] = queue.poll().point;
        }
        
        return output;
    }
}
