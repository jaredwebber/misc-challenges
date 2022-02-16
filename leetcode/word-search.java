

//curr process
class Solution {
    public boolean exist(char[][] board, String word) {
        boolean found = false;
        HashMap<Character, ArrayList<int[]>> letterPos = new HashMap<Character, ArrayList<int[]>>();
        
        for(int i = 0; i<board.length; i++){
            for(int j=0; j<board[0].length; j++){
               if(word.contains(String.valueOf(board[i][j]))){
                   ArrayList <int[]> temp = letterPos.get(board[i][j]);
                   if(temp == null){
                       temp = new ArrayList<int[]>();
                       temp.add(new int[]{i,j});
                       letterPos.put(board[i][j], temp);
                   }else{
                       temp.add(new int[]{i,j});
                       letterPos.put(board[i][j], temp);
                   }
               } 
            }
        }
        
        //search all word characters to find a path from char 0 to n
        boolean exhausted = false;
        while(!exhausted){
            for(char i: word){
                ArrayList<int[]> coords = letterPos.get(i);
                if(coords.size() == 0) return false;

                
                if()
                for(int j = 0; j<coords.size(); j++){
                    findPath()
                }

                if(letterPos.get(i).)
            }
        }
        
        //print all characters in the word in table
        for(char i: letterPos.keySet()){
            ArrayList<int[]> coords = letterPos.get(i);
            for(int j = 0; j<coords.size(); j++){
                int[] coord = coords.get(j);
                System.out.print("["+coord[0]+","+coord[1]+"],");
            }
            System.out.println(i);
        }
        
        return found;
    }
}

//temp working
class Solution {
    public boolean exist(char[][] board, String word) {
        boolean found = false;
        
        for(int i = 0; i<board.length; i++){
            for(int j=0; j<board[0].length; j++){
                //find first letter
                if(board[i][j] == word.charAt(0)){
                    int row = i;
                    int col = j;
                    HashMap<char, int[]> usedLetters = new HashMap<char, int[]>();
                    int[] currPos = new int[]{i,j};
                    usedLetters.add(board[i][j], currPos)
                    //find first letter of the word
                    //check all 4 directions around the letter
                    //continue process until stuck
                    
                    while(true){
                        if(row+1<board.length;)
                    }
                    
                }
            }
        }
        return found;
    }
}