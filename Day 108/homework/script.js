//1) კომენტარის სახით ახსენით რა არის localstorage და დაწვრილებით ჩამოაყალიბეთ იგი თქვენივე სიტყვებთ 
//2) ჩამოწერეთ დღეს ნასწავლი ყველა მეთოდი რომელიც უკავშირდება localstorage'ს ახსენით კომენტარის სახით და გააკეთეთ მაგალითებიც 

//3) კომენტარის სახით ჩამოაყალიბეთ რატომ ინახება ჩვენს მიერ შენახული ინფორმაცია string'ის სახით localstorage'ში 

//4) https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/javascript

//5) https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/javascript

//6) https://www.codewars.com/kata/54edbc7200b811e956000556/train/javascript

///7) https://www.codewars.com/kata/53ee5429ba190077850011d4/train/javascript

//8) https://www.codewars.com/kata/55a70521798b14d4750000a4/train/javascript

///9) https://www.codewars.com/kata/582cb0224e56e068d800003c/train/javascript

//10) https://www.codewars.com/kata/57f781872e3d8ca2a000007e/train/javascript




//1)
//localStorage — არის ბრაუზერის შიდა მეხსიერება, სადაც შეგვიძლია მონაცემების მუდმივად შენახვა key:value წყვილების სახით.



//2)
//
// 1. setItem(key, value)
// ინახავს მონაცემს localStorage-ში
//
//localStorage.setItem("name", "Giorgi");

//
//2. getItem(key)
// აბრუნებს შენახულ მონაცემს მითითებული key-ის მიხედვით

//let username = localStorage.getItem("name");
//console.log(username); 

//
//3. removeItem(key)
// შლის კონკრეტულ key-ს და მის მნიშვნელობას
//
//localStorage.removeItem("name");


//4. clear()
 //შლის localStorage-ში შენახულ ყველა მონაცემს

//localStorage.clear();


//5. key(index)
 //აბრუნებს კონკრეტული ინდექსის key-ს

//localStorage.setItem("color", "blue");
//localStorage.setItem("car", "BMW");
//console.log(localStorage.key(0)); 
//console.log(localStorage.key(1)); 

 //აბრუნებს რამდენი ელემენტია შენახული localStorage-ში

//console.log(localStorage.length);







//3)
// // localStorage მხოლოდ string ტიპის მონაცემებს ინახავს, რადგან იგი წარმოადგენს ბრაუზერის მეხსიერებაში არსებული მარტივი key-value საცავს,
// სადაც value ყოველთვის უნდა იყოს ტექსტური ფორმატის (string). 
// ამიტომ, როცა გვინდა ობიექტის, მასივის ან სხვა ტიპის მონაცემის შენახვა, 
// აუცილებელია მათი გარდაქმნა string ფორმატში JSON.stringify() მეთოდის მეშვეობით,
// ხოლო წამოღებისას  უკან გარდაქმნა ობიექტად JSON.parse() ფუნქციით.




//4)
function findSmallestInt(arr) {
  return Math.min(...arr);
}


//5)
function summation(num) {
  return (num * (num + 1)) / 2;
}


//6)
function countSheeps(sheep) {
  return sheep.filter(Boolean).length;
}


//7)
function doubleInteger(i) {
  return i * 2;
}

//8)
function greet(name) {
  return `Hello, ${name} how are you doing today?`;
}

//9)
function litres(time) {
  return Math.floor(time * 0.5);
}

//10)
function maps(x) {
  return x.map(n => n * 2);
}
