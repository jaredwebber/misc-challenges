//https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> cellsInRange(String s) {
        List<String> cells = new ArrayList<String>();
        int startNum = Integer.parseInt(String.valueOf(s.charAt(1)));
        char startChar = s.charAt(0);
        
        int letterDiff = s.charAt(3) - startChar;
        int numDiff =  Integer.parseInt(String.valueOf(s.charAt(4))) - startNum;        
        
        for(int i = 0; i<=letterDiff; i++){
            for(int j = startNum; j<=startNum+numDiff; j++){
                cells.add((char)(startChar + i)+""+j);
            }
        }
        
        return cells;
    }
}
