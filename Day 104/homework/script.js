







//1
function arrayPlusArray(arr1, arr2) {

  return arr1.concat(arr2).reduce((a, b) => a + b, 0);
}

//2
function stringToArray(string){
  return string.split(" ");
}

//3
function digitize(n) {
  return String(n).split("").map(Number).reverse();
}

//4
function numberToString(num) {
  return String(num);
}

//5
function removeChar(str){
  return str.slice(1, -1);
}

//6

//7
//8
//9