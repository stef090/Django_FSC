// var cell_array = document.getElementsByClassName("col-xs-1");
//
// for (cell of cell_array) {
//
// cell.addEventListener("click", function() {
//   if(cell.textContent==="X"){
//     cell.textContent="O";
//   }
//   cell.textContent = "X";
// })

//}

//Grab each field and assign Event Listener to it
for (var i = 1; i < 10; i++) {
  document.getElementById(i.toString()).addEventListener("click", function() {
    if(this.textContent === "X"){
      this.textContent = "O";
    }
    else {
      this.textContent = "X";
    }
  });
}


var restartButton = document.getElementById('restart');
restartButton.addEventListener("click", function() {
  var cell_array = document.getElementsByClassName("col-xs-1");
  for (cell of cell_array) {
    cell.textContent = "";
  }
})
