//https://leetcode.com/problems/watering-plants-ii/

class Solution {
    public int minimumRefill(int[] plants, int capacityA, int capacityB) {
        int refills = 0;
        int currA = capacityA;
        int currB = capacityB;

        for(int i = 0; i<plants.length/2; i++){
            if(plants[i]>currA){
                refills++;
                currA = capacityA;
            }
            currA -= plants[i];

            if(plants[plants.length-1-i]>currB){
                refills++;
                currB = capacityB;
            }
            currB-=plants[plants.length-1-i];
        }
        
        // check middle element
        if(plants.length % 2 != 0){
            if(currA<currB){
                if(plants[plants.length/2]>currB)
                    refills++;
            }else{
                if(plants[plants.length/2]>currA)
                    refills++;
            }
        }
        
        return refills;
    }
}
