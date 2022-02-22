//https://leetcode.com/problems/word-search/

class Solution {
    public boolean exist(char[][] board, String word) {
        boolean[][] visited = new boolean[board.length][board[0].length];
        
        for(int i = 0; i<board.length; i++){
            for(int j = 0; j<board[0].length; j++){
                if(word.charAt(0) == board[i][j]){
                    if(search(board, word, i,j,0, visited)) return true;
                }
            }
        }
        return false;
    }
    
    private boolean search(char[][] board, String word, int row, int col,int index, boolean[][] visited){
        if(index == word.length()) return true;
        if(row < 0 || row> board.length-1 || col<0 || col>board[0].length-1 || board[row][col]!=word.charAt(index) || visited[row][col]) return false;
        
        visited[row][col] = true;
        boolean continueSearch = 
            search(board, word, row+1, col, index+1, visited) ||
            search(board, word, row-1, col, index+1, visited) ||
            search(board, word, row, col+1, index+1, visited) ||
            search(board, word, row, col-1, index+1, visited);

        visited[row][col] = false;
        return continueSearch;
    }
}