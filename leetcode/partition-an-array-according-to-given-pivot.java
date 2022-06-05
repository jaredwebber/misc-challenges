//https://leetcode.com/problems/partition-array-according-to-given-pivot/

class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int[] partition = new int[nums.length];//will hold smaller values initially
        int partitionIndex = 0; //current index of partition
        int equal = 0; //number of elements equal to pivot
        int[] higher = new int[nums.length];//values larger thatn pivot
        int highIndex = 0;//current index in higher arr
        
        for(int i:nums){
            if(i == pivot) equal++;
            else if(i<pivot){
                partition[partitionIndex++] = i;
            }else{
                higher[highIndex++] = i;
            }
        }
        
        for(int i = 0; i<equal; i++){
            partition[partitionIndex++] = pivot;
        }
        
        for(int i = 0; i<highIndex; i++){
            partition[partitionIndex++] = higher[i];
        }
        
        return partition;
    }
}