//https://leetcode.com/problems/design-parking-system/

class ParkingSystem {
    private int[] spotsRemaining;
    public ParkingSystem(int big, int medium, int small) {
        spotsRemaining = new int[]{big, medium, small};
    }
    
    public boolean addCar(int carType) {
        if(spotsRemaining[carType-1] >0){
            spotsRemaining[carType-1]--;
            return true;
        }
        return false;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */
