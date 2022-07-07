// https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution {
    public int numberOfBeams(String[] bank) {
        int last = 0;
        int total = 0;
        int currCount = 0;
        char[] sequence;
        
        for(int i = 0; i<bank.length; i++){
            sequence = bank[i].toCharArray();
            currCount = 0;
            for(int j = 0; j<sequence.length; j++){
                if(sequence[j] == '1') currCount++;    
            }
            if(currCount > 0){
                total += last*currCount;
                last = currCount;
            }
        }
        
        return total;
    }
}
