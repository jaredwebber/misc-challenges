var fs = require('fs');
  
//input data as an array
var input = fs.readFileSync('input.txt', 'utf8').split("\n");

var ones = new Array(input[0].length);//ones array

for(var r = 0; r<input[0].length;r++){
    ones[r] = 0;
}


function readInput(){
   for(var i = 0; i<input.length; i++){
        for(var j = 0; j<input[i].length; j++){
            if(input[i].charAt(j) == "1"){
                ones[j]++;
            }
        }
   }

   for(var k = 0; k<ones.length; k++){
       if(ones[k]>=input.length/2){
           ones[k] = 1;
       }else{
           ones[k] = 0
       }
   }
}

function calcGamma(){
    var val = 0;
    for(var i = 0; i<ones.length;i++){
        if(ones[i] == 1){
            val+= Math.pow(2,ones.length-i-1);
        }   
    }
    return val;
}

function calcEpsilon(){
    var val = 0;
    for(var i = 0; i<ones.length;i++){
        if(ones[i] == 0){
            val+= Math.pow(2,ones.length-i-1);
        }   
    }
    return val;
}

readInput();

console.log(calcGamma() * calcEpsilon());
