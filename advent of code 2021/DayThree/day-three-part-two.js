var fs = require('fs');
  
//input data as an array
var input = fs.readFileSync('input.txt', 'utf8').split("\n");

//gas can either be 'oxygen' or 'co2'

function getValue(gas){
    var parentList = new Array();
    parentList.push(...input);
    
    var childList = new Array();
    var index = 0;
    
    while(parentList.length > 1){
        var goal = getDesiredDigit(parentList, index, gas);
        for(var i = 0; i< parentList.length; i++){
            if(parentList[i].charAt(index) == goal){
                childList.push(parentList[i]);
            }
        }
        index++;
        parentList = [];
        parentList.push(...childList);
        childList = [];
    }
    
    return parentList[0];
}

function getDesiredDigit(list, index, gas){
    var one = 0;
    var zero = 0;

    for(var i = 0; i<list.length; i++){
        if(list[i].charAt(index) == "0"){
            zero++;
        }else{
            one++
        }
    }

    if(gas == "oxygen"){
        if(one>=zero){
            return "1";
        }else{
            return "0";
        }
    }else{
        if(one>=zero){
            return "0";
        }else{
            return "1";
        }
    }
}

function binaryToDecimal(binary){
    var decimal = 0;
    for(var i = 0; i<binary.length;i++){
        if(binary[i] == 1){
            decimal+= Math.pow(2,binary.length-i-1);
        }   
    }
    return decimal;
}

console.log(binaryToDecimal(getValue("oxygen")) * binaryToDecimal(getValue("co2")));
