//https://leetcode.com/problems/word-search-ii/submissions/

/* Relatively inefficient, runs slow */

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        boolean[][] visited = new boolean[board.length][board[0].length];;
        ArrayList<String> wordList = new ArrayList<String>();
        
        for(String i:words){
            for(int j = 0; j<board.length; j++){
                for(int k = 0; k<board[0].length; k++){
                    if(board[j][k] == i.charAt(0))
                        if(search(board, visited, i,j,k,0))
                            if(!wordList.contains(i)) wordList.add(i);
                }
            }
        }
        
        return wordList;
    }
    
    private boolean search(char[][] board, boolean[][] visited, String word, int row, int col, int index){
        if(index ==  word.length()) return true;
        if(row<0 || row>=board.length || col<0 || col>=board[0].length || board[row][col] != word.charAt(index) || visited[row][col]) return false;
        
        visited[row][col] = true;
        boolean result = 
            search(board, visited, word, row+1, col, index+1) ||
            search(board, visited, word, row-1, col, index+1) ||
            search(board, visited, word, row, col+1, index+1) ||
            search(board, visited, word, row, col-1, index+1);
        visited[row][col] = false;
        
        return result;   
    }
}