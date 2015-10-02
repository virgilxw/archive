
//function to make a box
function box() {
	$(document).ready(function() {
		$("#container").append("<div class=box></div>");
	});
};

var input
//reset box
function reset() {
	$(".box").css("background-color", "#3399FF");
	var input = prompt('Type in the new width of the grid');
	console.log ("test")
};


//make grid
var input = 256;

for (var i = 0; i<input; i++) {
	box();
};


//change color on mousein
var color = "yellow";

$(document).ready(function() {
	$(".box").mouseover(function(){
		$(this).css("background-color", color);
	});
});


//test