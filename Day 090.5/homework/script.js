//1) ივარჯიშეთ for in და for of ზე და გააკეთეთ თითოეულზე 5 მაგალითი

//2) კომენტარის სახით ახსენით თქვენთვის ნასწავლი ყველა მეთოდი 

//3) კომენტარის სახით ახსენით რაში გვჭირდება რესპონსივი საიტზე

//4) დამატებით გააკეთეთ 5 8kyu და 5 7kyu ამოცანა



//1)


//1

let user = { name: "John", age: 25, country: "USA" };
for (let key in user) {
    console.log(key, ":", user[key]);
}
//2
let numbers = [10, 20, 30];
for (let index in numbers) {
    console.log("Index:", index, "Value:", numbers[index]);
}

//3
let word = "HELLO";
for (let i in word) {
    console.log(i, word[i]);
}
//4

let car = { brand: "BMW", model: "X5", year: 2020 };
for (let key in car) {
    console.log(`Property ${key} = ${car[key]}`);
}


//2)

// push() -> ამატებს ელემენტს მასივის ბოლოში
// pop() -> შლის ელემენტს მასივის ბოლოდან
// shift() -> შლის ელემენტს მასივის თავიდან
// unshift() -> ამატებს ელემენტს მასივის თავში
// slice(start, end) -> აკოპირებს მასივის ნაწილს (არ ცვლის ორიგინალს)
// splice(start, deleteCount, ...items) -> შლის/ამატებს/ცვლის ელემენტებს მასივში
// map() -> აბრუნებს ახალ მასივს თითოეულ ელემენტზე ფუნქციის შესრულებით
// filter() -> აბრუნებს ახალ მასივს მხოლოდ იმ ელემენტებით, რომლებიც აკმაყოფილებს პირობას
// reduce() -> ამცირებს მასივს ერთ მნიშვნელობამდე (მაგ: ჯამი)
// forEach() -> ასრულებს ფუნქციას თითოეულ ელემენტზე (არ აბრუნებს ახალ მასივს)
// find() -> აბრუნებს პირველ ელემენტს, რომელიც აკმაყოფილებს პირობას
// findIndex() -> აბრუნებს ინდექსს პირველი შესაბამისი ელემენტისთვის
// includes() -> ამოწმებს შეიცავს თუ არა მასივი/სტრიქონი მნიშვნელობას
// indexOf() -> აბრუნებს მნიშვნელობის ინდექსს
// sort() -> ალაგებს მასივს
// reverse() -> აბრუნებს მასივის ელემენტების მიმდევრობას
// split() -> ყოფს სტრიქონს მასივად
// join() -> აერთიანებს მასივს სტრიქონად
// toUpperCase() -> სტრიქონს გადააქცევს დიდ ასოებად
// toLowerCase() -> სტრიქონს გადააქცევს პატარა ასოებად
// trim() -> შლის ცარიელ ადგილებს სტრიქონის თავიდან და ბოლოდან



//3)
// რესპონსივი საჭიროა იმისთვის, რომ საიტი კარგად გამოიყურებოდეს ყველა მოწყობილობაზე

//4)
// 1
function opposite(num) {
  return -num;
}

// 2
function booleanToString(b) {
  return b.toString();
}

// 3
function sum(a, b) {
  return a + b;
}

// 4
function noSpace(str) {
  return str.replace(/\s/g, '');
}

// 5
function repeatStr(n, s) {
  return s.repeat(n);
}


// 5)

// 1) ყველაზე მოკლე სიტყვის სიგრძე
function findShort(s) {
  return Math.min(...s.split(" ").map(word => word.length));
}

// 2) მასივის ელემენტების ჯამი მინ/მაქს-ის გარეშე
function sumArray(arr) {
  if (!arr || arr.length <= 2) return 0;
  return arr.reduce((a, b) => a + b, 0) - Math.max(...arr) - Math.min(...arr);
}


