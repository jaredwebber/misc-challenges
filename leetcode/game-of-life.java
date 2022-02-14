//https://leetcode.com/problems/game-of-life/

class Solution {
    public void gameOfLife(int[][] board) {
        int[][] newBoard = new int[board.length][board[0].length];
        
        for(int i = 0; i<board.length; i++){
            for(int j = 0; j<board[0].length; j++){
                int friends = 0;
                if(j-1>=0 && i-1>=0 && board[i-1][j-1] == 1) friends++;//topleft
                if(i-1>=0 && board[i-1][j] == 1) friends++;//up
                if(j+1<board[0].length && i-1>=0 && board[i-1][j+1] == 1) friends++;//topright
                if(j-1>=0 && board[i][j-1] == 1) friends++;//left
                if(j+1<board[0].length && board[i][j+1] == 1) friends++;//right
                if(j-1>=0 && i+1<board.length && board[i+1][j-1] == 1) friends++;//bottomleft
                if(i+1<board.length && board[i+1][j] == 1) friends++;//bottom
                if(j+1<board[0].length && i+1<board.length && board[i+1][j+1] == 1) friends++;//bottomright
                
                if(board[i][j] == 1){
                    if(friends < 2 || friends>3){
                        newBoard[i][j] = 0;
                    }else{
                        newBoard[i][j] = 1;
                    }
                }else if(board[i][j] == 0 && friends == 3){
                    newBoard[i][j] = 1;
                }
                
                
            }
        }   
        
        for(int i = 0; i<board.length; i++){
            for(int j = 0; j<board[0].length; j++){
                board[i][j] = newBoard[i][j];
            }
        }
    }
}
