class Board{

    constructor(boardList, size){
        this.boardSize = size;
        this.board = boardList;
        this.sumUnfilled = this.getTotalSum();
    }

    isGameOver(num){
        var answer = -1;
        

        //Check horizontal lines
        var currCount = 0;
        for(var i = 0; i<this.boardSize;i++){
            for(var j = 0; j<this.boardSize; j++){
                if(this.board[i][j] === 'X'){
                    currCount++;
                }
            }
            if(currCount === this.boardSize){
                answer = num;
                console.log("GAME OVER")
            }
            currCount = 0;
        }

        //Check vertical lines
        currCount = 0;
        for(var i = 0; i<this.boardSize;i++){
            for(var j = 0; j<this.boardSize; j++){
                if(this.board[j][i] === 'X'){
                    currCount++;
                }
            }
            console.log(currCount);
            if(currCount === this.boardSize){
                answer = num;
            }
            currCount = 0;
        }

        /* not required :(
        //Check diagonals
        var BLtoTR = 0;
        var TLtoBR = 0;
        for(var i = 0; i<this.boardSize; i++){
            if(this.board[i][i] === 'X'){
                TLtoBR++;
            }
            if(this.board[BOARD_SIZE-1-i][i] === 'X'){
                BLtoTR++;
            }
        }
        if(BLtoTR === BOARD_SIZE || TLtoBR === BOARD_SIZE){
            answer = num;
        }

        console.log(this.board)
        console.log("\n"+num)
        */

        //check if and line in the board has been filled (X)
        //including diagonals?
        console.log(this.board)
        if(answer>0){
            return answer*this.sumUnfilled;
        }
        return 0;
    }

    addNumber(num){
        for(var i = 0; i<5;i++){
            var row = this.board[i];
            for(var j = 0; j<5; j++){
                if(row[j] == num){
                    row[j] = 'X';
                    this.sumUnfilled -= num;
                }
            }
        }

        return this.isGameOver(num);
    } 

    getTotalSum(){
        var sum = 0;
        for(var i = 0; i<this.boardSize;i++){
            var row = this.board[i];
            for(var j = 0; j<this.boardSize; j++){
                sum += parseInt(row[j]);
            }
        }
        return sum;
    }
}


const { strictEqual } = require('assert');
var fs = require('fs');
const { runInThisContext } = require('vm');
  
//input data as an array
var input = fs.readFileSync('input.txt', 'utf8').split("\n");
var listOfNums = input[0].split(",");
var boards = new Array();
var BOARD_SIZE = 5;

var index = 1;
var curr = 0;

while(index<input.length){
    curr = 0;
    var table = new Array();
    
    while(curr<BOARD_SIZE){
        if(!input[index].match(/^ *$/)){
            table.push(input[index].trim().split(/\s+/));
            curr++;
        }
        index++;
    }
    boards.push(new Board(table,BOARD_SIZE));
}


var count = 0;
var answer = 0;
while(count< listOfNums.length && answer<=0){
    for(var i = 0; i<boards.length; i++){
        answer = boards[i].addNumber(listOfNums[count]);
        if(answer>0){
            console.log(answer);
            break;
        }
    }
    
    count ++;
}
