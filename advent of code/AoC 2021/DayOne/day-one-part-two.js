var fs = require('fs');
  
//input data as an array
var input = fs.readFileSync('input.txt', 'utf8').split("\n");
for(i in input) input[i] = parseInt(input[i]);

function threeSumIncreases(){
    var sum;
    var lastSum;
    var count = 0;

    lastSum = input[0]+input[1]+input[2];

    for(var i = 1; i<input.length-2; i++){
        sum = input[i]+input[i+1]+input[i+2];
        if(lastSum<sum) count++;
        lastSum = sum;  
    }

    return count;
}

console.log(threeSumIncreases());

