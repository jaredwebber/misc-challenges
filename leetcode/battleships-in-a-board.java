// https://leetcode.com/problems/battleships-in-a-board

class Solution {
    public int countBattleships(char[][] board) {
        int count = 0;
        for(int i = 0; i<board.length; i++){
            for(int j = 0; j<board[0].length; j++){
                if(board[i][j] == 'X'){
                    count++;
                    flood(board, i, j);
                }
            }
        }
        return count;
    }

    private void flood(char[][] board, int i, int j){
        if(i >=0 && i < board.length && j >=0 && j < board[0].length && board[i][j] == 'X'){
            board[i][j] = '.';
            flood(board, i+1, j);
            flood(board, i-1, j);
            flood(board, i, j+1);  
            flood(board, i, j-1);
        }
    }
}
