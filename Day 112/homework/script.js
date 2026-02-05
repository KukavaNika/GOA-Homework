// 1. შექმენით ფუნქცია, რომელიც იღებს რიცხვების მასივს და თითოეულ რიცხვს ბეჭდავს for ციკლის გამოყენებით.
// 2. შექმენით სახელების მასივი, შემდეგ, გამოიყენეთ for ციკლი თითოეული სახელის და მისი პოზიციის დასაბეჭდად.
// 3. შექმენით პროგრამა, რომელიც მასივში თითოეულ რიცხვს ამრავლებს 2-ზე და შედეგს ბეჭდავს მათ for ციკლის გამოყენებით.
// 4. დაწერეთ ფუნქცია, რომელიც for ციკლის გამოყენებით ითვლის მასივში რამდენი ელემენტია 10-ზე მეტი.
// 5. გამოიყენეთ for ციკლი მასივის ყველა ელემენტის შესაჯამებლად და საბოლოო შედეგის დასაბეჭდად.



//1
function printNumbers(arr) {
  for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
  }
}

printNumbers([1, 2, 3, 4, 5]);


//2
let names = ["Nika", "Ana", "Giorgi"];

for (let i = 0; i < names.length; i++) {
  console.log(i + " - " + names[i]);
}


//3
let numbers = [2, 4, 6, 8];

for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i] * 2);
}



//4
function countMoreThanTen(arr) {
  let count = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > 10) {
      count++;
    }
  }

  return count;
}

console.log(countMoreThanTen([5, 12, 20, 8, 15]));



//5
let nums = [1, 2, 3, 4, 5];
let sum = 0;

for (let i = 0; i < nums.length; i++) {
  sum += nums[i];
}

console.log(sum);

