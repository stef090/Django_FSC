const numberOfColumns = 7;
const numberOfRows = 6;


$(document).ready(function(){

  var playerOne = prompt("Welcome to Connect Four! Please input your name(Player 1):");
  var playerTwo = prompt("Welcome to Connect Four! Please input your name(Player 2):");
  var activePlayer = playerOne;
  var playerOneChips = [];
  var playerTwoChips = [];
  var playerClasses = {};
  var win = false;
  playerClasses[playerOne] = 'player1active';
  playerClasses[playerTwo] = 'player2active';
  // var playerClasses = {
  //   playerOne: 'player1active',
  //   playerTwo: 'player2active'
  // };
  var columns = [];
  $('h3').html('<span class="player1active">'+activePlayer+'</span>, it is your turn!');

  //Put rows and columns into an array to hold their indexes
  for (var i = 0; i < numberOfColumns; i++) {
    var column = [];
    for(var j=0; j < numberOfRows; j++){
      column.push((j*numberOfColumns)+i);
    }
    columns.push(column);
  }

  $('td > div').click(function functionName() {
    //console.log(activePlayer);
    //console.log($('td').index(this));
    //console.log('Table data clicked!');
    var chips = $('td > div');
    for(column in columns){
      if(columns[column].indexOf(chips.index(this))!=-1){
        chip = columns[column].pop();
        if(activePlayer==playerOne){
          chips.eq(chip).addClass('player1');
          playerOneChips.push(chip);
          if(playerOneChips.length >= 4){
            if(checkWin(playerOneChips)){
              announcePlayer(playerOne, playerClasses, true);
              win = true;
            };
          }
          activePlayer = playerTwo;

        }
        else {
          chips.eq(chip).addClass('player2');
          playerTwoChips.push(chip);
          if(playerTwoChips.length >= 4){
            if(checkWin(playerTwoChips)){
              announcePlayer(playerTwo, playerClasses, true);
              win = true;
            };
          }
          activePlayer = playerOne;
        }
      }
    }
    if(win!=true){
    announcePlayer(activePlayer,playerClasses, false);
    }

  })
});

function announcePlayer(activePlayer, playerClasses, win){
  if(win){
    $('td > div').off("click");
    $('h3').html('<span class="'+playerClasses[activePlayer]+'">'+activePlayer+'</span> is the winner, congratulations!');
  }
  else {
    $('h3').html('<span class="'+playerClasses[activePlayer]+'">'+activePlayer+'</span>, it is your turn!');
  }
}

function checkWin(array){
  array.sort(function compare(a,b){
  if(a<b){
    return -1;
  }
  if(a>b){
    return 1;
  }
  return 0;
  });
  return checkHorizontal(array) || checkVertical(array) || checkDiagonal(array);
  //checkVertical(array);
  //checkDiagonal(array);

}

//Check for win horizontally
function checkHorizontal(array){
  for (var i = 0; i < array.length; i++) {
    if(array[i] && array.indexOf(array[i]+1)!=-1 && array.indexOf(array[i]+2)!=-1 && array.indexOf(array[i]+3)!=-1){
      return true;
    }
  }
  return false;

}

//Check for win vertically, using number of columns as step
function checkVertical(array){
  for (var i = 0; i < array.length; i++) {
      if(array[i] && array.indexOf(array[i]+numberOfColumns)!=-1 && array.indexOf(array[i]+numberOfColumns*2)!=-1 && array.indexOf(array[i]+numberOfColumns*3)!=-1 ){
        return true;
      }
  }
  return false;

}

function checkDiagonal(array){
  for (var i = 0; i < array.length; i++) {
    if(array[i] > numberOfColumns*Math.floor(numberOfRows/2)-1){
      if(checkDiagonalUpper(array,array[i])){
        return true;
      }
    }
    else{
      if(checkDiagonalLower(array,array[i])){
        return true;
      }
    }
  }
  return false;
}

function checkDiagonalUpper(array, number){
 //Check diagonal in the upper right direction
 if(number && array.indexOf(number-numberOfColumns+1)!=-1 && array.indexOf(number-(numberOfColumns*2)+2)!=-1 && array.indexOf(number-(numberOfColumns*3)+3)!=-1){
   return true;
 }
 //Check diagonal in the upper left direction
 else if(number && array.indexOf(number-numberOfColumns-1)!=-1 && array.indexOf(number-(numberOfColumns*2)-2)!=-1 && array.indexOf(number-(numberOfColumns*3)-3)!=-1){
     return true;
   }
 return false;
}

function checkDiagonalLower(array, number){
  //Check diagonal in the lower right direction
  if(number && array.indexOf(number+numberOfColumns+1)!=-1 && array.indexOf(number+(numberOfColumns*2)+2)!=-1 && array.indexOf(number+(numberOfColumns*3)+3)!=-1){
    return true;
  }
  //Check diagonal in the lower left direction
  else if(number && array.indexOf(number+numberOfColumns-1)!=-1 && array.indexOf(number+(numberOfColumns*2)-2)!=-1 && array.indexOf(number+(numberOfColumns*3)-3)!=-1){
      return true;
    }
  return false;
}
