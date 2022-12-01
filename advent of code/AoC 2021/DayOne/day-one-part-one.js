var fs = require('fs');
  
//input data as an array
var input = fs.readFileSync('input.txt', 'utf8').split("\n");

function howManyIncreases(){
    var count = 0;
    for(var i=1; i<=input.length; i++){
        if(input[i]>input[i-1]) count++;
    }
    return count;
}

console.log(howManyIncreases());
//correct answer 1832 - this returns 1830 for whatever reason

