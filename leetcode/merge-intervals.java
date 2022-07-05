// https://leetcode.com/problems/merge-intervals/

import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[][] merge(int[][] intervals) {
        ArrayList<int[]> intervalList = new ArrayList<int[]>();
        
        Arrays.sort(intervals, (one, two) -> Integer.compare(one[0], two[0]));
        
        int index = 0;
        while(index < intervals.length){
            int[] interval = new int[]{intervals[index][0], intervals[index][1]};
            index++;
            while(index < intervals.length && intervals[index][0] >= interval[0] && intervals[index][0] <= interval[1]){
                interval[1] = Math.max(interval[1], intervals[index++][1]);
            }
            intervalList.add(interval);
        }

        return intervalList.toArray(new int[intervalList.size()][2]);
    }
}

