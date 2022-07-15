// https://leetcode.com/problems/time-based-key-value-store/ 

import java.util.HashMap;

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */


// Relatively Inefficient
// Could use binary search or tree construction
class TimeMap {
    HashMap<String, HashMap<Integer, String>> map;
    
    public TimeMap() {
        map = new HashMap<String, HashMap<Integer, String>>();
    }
    
    public void set(String key, String value, int timestamp) {
        HashMap<Integer, String> innerMap = map.getOrDefault(key, new HashMap<Integer, String>());
        innerMap.put(timestamp, value);
        map.put(key, innerMap);
    }
    
    public String get(String key, int timestamp) {
        if(map.get(key) == null) return "";
        HashMap<Integer, String> innerMap = map.get(key);
        for(int i = timestamp; i>=0; i--){
            if(innerMap.get(i) != null) return innerMap.get(i);
        }
        return "";
    }
}
