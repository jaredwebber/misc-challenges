// https://leetcode.com/problems/surrounded-regions/

class Solution {
    public void solve(char[][] board) {
        // First and Last columns
        for(int i = 0; i<board.length; i++){
            if(board[i][0] == 'O') markFreeRegions(board, i, 0);
            if(board[i][board[0].length-1] == 'O') markFreeRegions(board, i, board[0].length-1);
        }
        
        // Top and Bottom Rows
        for(int i = 1; i<board[0].length-1; i++){
            if(board[0][i] == 'O') markFreeRegions(board, 0, i);
            if(board[board.length-1][i] == 'O') markFreeRegions(board, board.length-1, i);
        }
        
        // Capture 0s, replace Free places with O
        for(int i = 0; i<board.length; i++){
            for(int j = 0; j<board[0].length; j++){
                if(board[i][j] == 'O') board[i][j] = 'X';
                if(board[i][j] == 'F') board[i][j] = 'O';
            }
        }
    }
    
    public void markFreeRegions(char[][] board, int i, int j){
        if(i >= 0 && j >= 0 && i < board.length && j < board[0].length && board[i][j] == 'O'){
            board[i][j] = 'F';
            markFreeRegions(board, i+1, j);
            markFreeRegions(board, i-1, j);
            markFreeRegions(board, i, j+1);
            markFreeRegions(board, i, j-1);
        }
    }
}
