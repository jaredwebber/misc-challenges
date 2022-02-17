//https://leetcode.com/problems/pascals-triangle/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> tri = new ArrayList<List<Integer>>();
        List<Integer> rowOne = new ArrayList<Integer>(Arrays.asList(1));
        List<Integer> rowTwo = new ArrayList<Integer>(Arrays.asList(1,1));
        
        for(int i = 1; i<=numRows; i++){
            if(i == 1){
                tri.add(rowOne);
            }
            else if(i == 2){
                tri.add(rowTwo);
            }else {
                ArrayList<Integer> currRow = new ArrayList<Integer>();
                currRow.add(1);
                for(int j = 0; j<((tri.get(i-2).size())-1); j++){
                    currRow.add(tri.get(i-2).get(j)+tri.get(i-2).get(j+1));
                }
                currRow.add(1);
                tri.add(currRow);
            }
        }
        return tri;
    }
}
