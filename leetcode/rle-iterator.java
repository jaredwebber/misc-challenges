//https://leetcode.com/problems/rle-iterator/

class RLEIterator {
    int[] rle;
    int index;
    
    public RLEIterator(int[] encoding) {
        rle = encoding;
        index = 0;
    }
    
    public int next(int n) {       
        if(index>=rle.length) return -1;
        if(rle[index] == 0) index+=2;
        
        while(n > rle[index]){
            n-= rle[index];
            index+=2;
            if(index>=rle.length) return -1;
        }
        rle[index]-=n;
        return rle[index+1];
    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator obj = new RLEIterator(encoding);
 * int param_1 = obj.next(n);
 */
