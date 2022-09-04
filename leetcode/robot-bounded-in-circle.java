// https://leetcode.com/problems/robot-bounded-in-circle/

import java.util.HashSet;

class Solution {

    // More Optimized Strategy
    public boolean isRobotBounded(String instructions) {
        int x = 0;
        int y = 0;
        char dir = 'N';
        char[] inst = instructions.toCharArray();
        
        for(int j = 0; j<inst.length; j++){
            if(inst[j] == 'L'){
                switch(dir){
                    case 'N': dir = 'W'; break;
                    case 'E': dir = 'N'; break;
                    case 'S': dir = 'E'; break;
                    case 'W': dir = 'S'; break;
                }
            }else if(inst[j] == 'R'){
                switch(dir){
                    case 'N': dir = 'E'; break;
                    case 'E': dir = 'S'; break;
                    case 'S': dir = 'W'; break;
                    case 'W': dir = 'N'; break;
                }
            }else{
                switch(dir){
                    case 'N': y++; break;
                    case 'E': x++; break;
                    case 'S': y--; break;
                    case 'W': x--; break;
                }
            }
        }
        
        return (x == 0 && y == 0) || dir != 'N';
    }

    // Brute Force Approach
    class Pos{
        int x;
        int y;
        public Pos(int x, int y){
            this.x = x;
            this.y = y;
        }
        
        @Override
        public int hashCode() {
            final int prime = 31;
            int result = 1;
            result = prime * result + x;
            result = prime * result + y;
            return result;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj)
                return true;
            if (obj == null)
                return false;
            if (getClass() != obj.getClass())
                return false;
            Pos other = (Pos) obj;
            if (x != other.x)
                return false;
            if (y != other.y)
                return false;
            return true;
        }
    }
    
    public boolean isRobotBoundedBruteForce(String instructions) {
        HashSet<Pos> visited = new HashSet<Pos>();
        int x = 0;
        int y = 0;
        char dir = 'N';
        char[] inst = instructions.toCharArray();
        
        for(int i = 0; i<25; i++){ // arbitrary number choice
            boolean cycle = true;
            for(int j = 0; j<inst.length; j++){
                Pos curr = new Pos(x, y);
                if(!visited.contains(curr)) {
                    cycle = false;
                }
                visited.add(curr);
                
                if(inst[j] == 'L'){
                    switch(dir){
                        case 'N': dir = 'W'; break;
                        case 'E': dir = 'N'; break;
                        case 'S': dir = 'E'; break;
                        case 'W': dir = 'S'; break;
                    }
                }else if(inst[j] == 'R'){
                    switch(dir){
                        case 'N': dir = 'E'; break;
                        case 'E': dir = 'S'; break;
                        case 'S': dir = 'W'; break;
                        case 'W': dir = 'N'; break;
                    }
                }else{
                    switch(dir){
                        case 'N': y++; break;
                        case 'E': x++; break;
                        case 'S': y--; break;
                        case 'W': x--; break;
                    }
                }
            }
            if(cycle) return true;
        }
        return false;
    }
}
