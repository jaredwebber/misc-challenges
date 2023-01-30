//https://leetcode.com/problems/insert-interval/

import java.util.ArrayList;

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int[][] outArrays = null;
        ArrayList<int[]> newIntervals = new ArrayList<int[]>();
        int index = 0;
                
        while(index < intervals.length){
            if(newInterval != null && (newInterval[0] <= intervals[index][1] || newInterval[0]<=intervals[index][0])){
                while(index < intervals.length && (newInterval[1] >= intervals[index][0] || newInterval[1]>=intervals[index][0])){
                    newInterval[0] = Math.min(newInterval[0], intervals[index][0]);
                    newInterval[1] = Math.max(intervals[index][1], newInterval[1]);
                    index++;
                }
                newIntervals.add(newInterval);
                newInterval = null;
            }else{
                newIntervals.add(intervals[index]);
                index++;
            }
        }
        
        if(newInterval != null || intervals.length == 0) newIntervals.add(newInterval);     
        
        outArrays = new int[newIntervals.size()][2];
        for(int i = 0; i<newIntervals.size(); i++){
            outArrays[i] = newIntervals.get(i);
        }
        
        return outArrays;
    }
}