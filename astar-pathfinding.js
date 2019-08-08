function removeFromArray(arr, elt) {
	for (var i = arr.length - 1; i >= 0; i--) {
		if(arr[i] === elt) {
			arr.splice(i,0);
		}
	}
}


var cols = 5;
var rows = 5;
var WIDTH = 400;
var HEIGHT = 400;
var grid = new Array(cols);

var openSet = [];
var closedSet = [];

var start;
var end;
var w, h;
var ctx;

function Spot(i,j) {
	this.i = i;
	this.j = j;
	this.f = 0;
	this.g = 0;
	this.h = 0;
	this.neighors = [];

	this.show = function(color) {
	  if(color==="white"){
        ctx.strokeStyle = "#000000";
	    ctx.strokeRect(this.i*w, this.j*h, w, h); 
	    } else{
		ctx.fillStyle = "#009900";
        ctx.fillRect(this.i*w, this.j*h, w, h);
       }
	}

	this.addNeighbors = function(grid) {
		var i = this.i;
		var j = this.j;

		if (i < cols -1 ) {
        this.neighors.push(grid[i + 1][j]);
        }
        if (i > 0) {
        this.neighors.push(grid[i - 1][j]);
        }
        if(j < rows -1){
        this.neighors.push(grid[i][j + 1]);
        }
        
        if( j > 0) {
        this.neighors.push(grid[i][j - 1]);
        }
	}
}

if (typeof console == "undefined") var console = { log: function() {} };
function onload()
{  
	w = WIDTH / cols;
	h = HEIGHT / rows;

	
	ctx = document.getElementById('ctx').getContext('2d');
	console.log("It works!");
    
    ///Making a 2d array
	for (var i = 0; i < cols; i++) {
		grid[i] = new Array(rows);
    }		
	
	for (var i = 0; i < cols; i++) {
	  
	  for(var j = 0; j < rows; j++) {

	  	grid[i][j] = new Spot(i, j);
	  }
	}
    
    for (var i = 0; i < cols; i++) {
	  
	  for(var j = 0; j < rows; j++) {

	  	grid[i][j].addNeighbors(grid);
	  }
	}
    start = grid[0][0];
    end   = grid[cols-1][rows-1];

    openSet.push(start);
    // while(true){
    // //draw();
    // }
    draw();

	console.log(grid);
}

function draw(){
	if(openSet.length > 0){
		//we can keep going

	var winner = 0;
	for (var i = 0; i < openSet.length; i++) {
       
       if (openSet[i].f < openSet[winner].f) {

       	 winner = i;
       }
	}
     
    var current = openSet[winner]; 
	if (openSet[winner] === end) {
		console.log("DONE!")
	}

	//openSet.remove(current);
	removeFromArray(openSet, current);
	closedSet.push(current);

	} else {

		//no solution 
	}
   
   for (var i = 0; i < cols; i++) {
   	for ( var j = 0; j < rows; j++ ) {

   		grid[i][j].show("white");
   	}
   }

   for (var i =0; i< closedSet.length; i++) {

   	closedSet[i].show("red");
   }

    for (var i =0; i< openSet.length; i++) {

   	openSet[i].show("green")
   }

}


