// https://leetcode.com/problems/lru-cache

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */

import java.util.HashMap;

class LRUCache {
    class Node {
        int val;
        int key;
        Node prev;
        Node next;

        Node(){
            this.val = 0;
            this.key = 0;
            this.prev = null;
            this.next = null;
        }

        Node(int val, int key){
            this.val = val;
            this.key = key;
            this.prev = null;
            this.next = null;
        }
    }

    class LL {
        Node head;
        Node tail;

        LL(){
            this.head = new Node();
            this.tail = new Node();
            this.head.next = tail;
            this.tail.prev = head;
        }

        void insert(Node node){
            node.next = head.next;
            head.next.prev = node;
            node.prev = head;
            head.next = node;
        }

        void remove(Node node){
            node.prev.next = node.next;
            node.next.prev = node.prev;
        }

        int removeLast(){
            int key = tail.prev.key;
            tail = tail.prev;
            return key;
        }
    }

    HashMap<Integer, Node> cache;
    LL list;
    int capacity;

    public LRUCache(int capacity) {
        this.cache = new HashMap<Integer, Node>();
        this.list = new LL();
        this.capacity = capacity;
    }
    
    public int get(int key) {
        if(cache.get(key) == null) return -1;
        Node curr = cache.get(key);
        list.remove(curr);
        list.insert(curr);
        return curr.val;
    }
    
    public void put(int key, int value) {
        if(cache.get(key) == null && cache.size() == capacity){
            cache.remove(list.removeLast());
        }else if(cache.get(key) != null){
            list.remove(cache.get(key));
        }
        Node node = new Node(value, key);
        list.insert(node);
        cache.put(key, node);
    }
}
