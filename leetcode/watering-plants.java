//https://leetcode.com/problems/watering-plants/

class Solution {
    public int wateringPlants(int[] plants, int capacity) {
        int steps = 0;
        int currCapacity = capacity;
        for(int i = 0; i<plants.length; i++){
            if(currCapacity<plants[i]){
                steps+=2*i;
                currCapacity = capacity;
            }
            currCapacity-=plants[i];
            steps++;
        }
        return steps;
    }
}
