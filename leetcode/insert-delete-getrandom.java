//https://leetcode.com/problems/insert-delete-getrandom-o1/
import java.util.HashMap;

class RandomizedSet {
    private HashMap<Integer, Integer> storage;
    
    public RandomizedSet() {
        storage = new HashMap<Integer, Integer>();
    }
    
    public boolean insert(int val) {
        boolean out = storage.get(val)==null;
        if(out) storage.put(val, 0);
        return out;
    }
    
    public boolean remove(int val) {
        boolean out = storage.get(val)!=null;
        if(out) storage.remove(val);
        return out;
    }
    
    public int getRandom() {
        return (int)storage.keySet().toArray()[(int)Math.floor(Math.random()*(storage.size()))]; 
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */