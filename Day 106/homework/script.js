


//1) https://www.codewars.com/kata/523b4ff7adca849afe000035/train/javascript

//2) https://www.codewars.com/kata/54edbc7200b811e956000556/train/javascript

//3) https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/javascript

///4) https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/javascript

//5) https://www.codewars.com/kata/53dc54212259ed3d4f00071c/train/javascript

//6) https://www.codewars.com/kata/53af2b8861023f1d88000832/train/javascript



//1
function greet() {
  return "hello world!";
}

//2
function countSheeps(sheep) {
  return sheep.filter(Boolean).length;
}

//3
function century(year) {
  return Math.ceil(year / 100);
}

//4
function basicOp(operation, value1, value2){
  switch(operation){
    case '+': return value1 + value2;
    case '-': return value1 - value2;
    case '*': return value1 * value2;
    case '/': return value1 / value2;
    default: return null;
  }
}

//5
function sum(numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}

//6
//ვერ გავაკეტე