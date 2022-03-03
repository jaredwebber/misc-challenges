//https://leetcode.com/problems/design-an-ordered-stream/

import java.util.ArrayList;
import java.util.List;

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream obj = new OrderedStream(n);
 * List<String> param_1 = obj.insert(idKey,value);
 */

class OrderedStream {
    int currPointer = 0;
    String[] blocks;
    public OrderedStream(int n) {
        blocks = new String[n];
    }
    
    public List<String> insert(int idKey, String value) {
        this.blocks[idKey-1] = value;
        List<String> chunks = new ArrayList<String>();
        while(currPointer<blocks.length && blocks[currPointer]!=null){
            chunks.add(blocks[currPointer++]);
        }
        return chunks;
    }
}
