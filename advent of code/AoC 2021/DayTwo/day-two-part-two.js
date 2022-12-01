var fs = require('fs');
  
//input data as an array
var input = fs.readFileSync('input.txt', 'utf8').split("\n");

function trackCourse(){
    var horz = 0;
    var depth = 0;
    var aim = 0;
    for(i in input){
        var instruction = input[i].split(" ");
        switch(instruction[0]){
            case "forward":
                horz+=parseInt(instruction[1]);
                depth+=aim*parseInt(instruction[1]);
                break;
            case "down":
                aim+=parseInt(instruction[1]);
                break;
            case "up":
                aim-=parseInt(instruction[1]);
                break;
            
        }
    }
    return horz*depth;
}

console.log(trackCourse());
