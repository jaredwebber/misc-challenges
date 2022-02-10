//https://leetcode.com/problems/lru-cache/

//Time limit exceeded:

import java.util.HashMap;

class LRUCache {
    
    private int accessTime = 0;
    private HashMap<Integer, Node> cache;
    private int maxCapacity;
    
    class Node{
        int accessTime;
        int value;
        
        private Node(int value, int accessTime){
            this.accessTime = accessTime;
            this.value = value;
        }
    }
    
    public LRUCache(int capacity) {
        cache = new HashMap<Integer, Node>(capacity); 
        maxCapacity = capacity;
    }
    
    public int get(int key) {
        accessTime++;
        Node node = cache.get(key);

        if(node != null){
            node.accessTime = accessTime;
            cache.put(key, node);
            return node.value;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        accessTime++;
        
        //check if key exists
        Node node = cache.get(key);
        if(node != null){
            node.accessTime = accessTime;
            node.value = value;
            cache.put(key, node);
            return;
        }
        
        //key not found
        if(cache.size() < maxCapacity){
            //insert new Node into cache
            cache.put(key, new Node(value, accessTime));
            node = cache.get(key);
        }else{
            int oldestAccess = Integer.MAX_VALUE;
            int oldKey = 0;
            for(int keyFromSet : cache.keySet()){
                node = cache.get(keyFromSet);
                if(node.accessTime < oldestAccess){
                    oldestAccess = node.accessTime;
                    oldKey = keyFromSet;
                }
            }
            cache.remove(oldKey);
            cache.put(key, new Node(value, accessTime));
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */