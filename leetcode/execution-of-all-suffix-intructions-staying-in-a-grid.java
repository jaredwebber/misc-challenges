//https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

class Solution {
    public int[] executeInstructions(int n, int[] startPos, String s) {
        int[] answer = new int[s.length()];
        int[] currPos;
        int count = 0;
        
        for(int i = 0; i<s.length();i++){
            count = i;
            currPos = new int[]{startPos[0], startPos[1]};
            while(count<s.length())
            {
                if(s.charAt(count) == 'R') currPos[1]++;
                else if(s.charAt(count) == 'L') currPos[1]--;
                else if(s.charAt(count) == 'D') currPos[0]++;
                else currPos[0]--;
                
                if(currPos[0] >= 0 &&
                  currPos[0]<n && 
                  currPos[1] >= 0 &&
                  currPos[1]<n) count++;
                else break;
            }
            
            answer[i] = count-i; 
        }
        
        return answer;
    }
}
