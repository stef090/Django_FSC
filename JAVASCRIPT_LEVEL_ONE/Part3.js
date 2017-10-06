var weight_pds=prompt("What is the weight in pounds?")
alert("The weight in kilograms is: " + weight_pds * 0.454 + " kg" )

console.log("Conversion complete!");

arr = [1,2,3,4,5,6]

for (var i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}

for (var num in arr) {
  if (num.hasOwnProperty()) {
    console.log(num);
  }
}
