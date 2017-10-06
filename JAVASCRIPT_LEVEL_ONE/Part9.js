var firstName = prompt("What is your first name?");
var lastName = prompt("What is your last name?");
var age = prompt("How old are you?");
var height = prompt("How tall are you?");
var petName = prompt("What is the name of your pet?")

if((firstName[0] == lastName[0])&&(age>20 && age<30)&&height>=170&&petName[petName.length-1]=='y'){
  console.log("You passed the spy test!");
}
else {
  console.log("Nothing to see here...");
}
