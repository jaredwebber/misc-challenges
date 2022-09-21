// https://leetcode.com/problems/valid-sudoku/

import java.util.HashSet;

class Solution {
    
    class Pair{
        int unit;
        int val;
        Pair(int unit, int val){
            this.unit = unit;
            this.val = val;
        }
        
        public int hashCode() {
            return unit * 31 + val * 31;
        }
        
        public boolean equals( Object other ) {
            if(this == other) return true;
            if(other instanceof Pair) {
                Pair p2 = (Pair) other;
                return this.unit == p2.unit &&                        
                this.val == p2.val;
            }
            return false;
        }
    }
    
    public boolean isValidSudoku(char[][] board) {
        HashSet<Pair> rows = new HashSet<Pair>();
        HashSet<Pair> cols = new HashSet<Pair>();
        HashSet<Pair> blocks = new HashSet<Pair>();
        int blockRow = 0;
        
        for(int i = 0; i<board.length; i++){
            for(int j = 0; j<board[0].length; j++){
                if(board[i][j] != '.'){
                    if(!cols.add(new Pair(i, board[i][j])) ||
                       !rows.add(new Pair(j, board[i][j])) || 
                       !blocks.add(new Pair(((i/3) + (j/3) + blockRow), board[i][j]))){
                        return false;
                    }
                }
            }
            if((i+1) /3 > i/3) blockRow+=2;
        }
        
        return true;
    }
}
