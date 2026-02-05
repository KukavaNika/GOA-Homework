



//1) დაბეჭდეთ for loops-ის დახმარებით კენტრი რიცხვები 1-დან 76-მდე/

//2) შექმენით ობიექტი, რომელშიც შეინახავთ თქვენთვის სასურველ key და value-ებს. თქვენი დავალებაა for in iterator-ის დახმარებით დაბეჭდოთ ობიექტში მყოფი ყველა key და value.

//3) შექმენით 6 ელემენტიანი სია, თქვენი დავალებაა დაბეჭდოთ ამ სიაში მყოფი ყველა ელემენტი for of iterator-ის დახმარებით.

//4) კომენტარების სახით თქვენი სიტყვებით ახსენით რა არის localStorage და მისი მეთოდები.

//5) localStorage-სა და .setItem() ფუნქციის დახმარებით შეინახეთ 7 მნიშვნელობა storage-ში თქვენთვის სასურველი key და value-ები.

//6) წინა დავალებაში გაკეთებულ localStorage-ში შენახული მნიშვნელობებიდან ამოშალეთ .removeItem() ფუნქციის დახმარებით ნებისმიერი 2 მნიშვნელობა.

///7) დაბეჭდეთ და console-ში გამოიტანეთ თქვენი localStorage-ი სიგრძე .length მეთოდის დახმარებით.

///8) localStorage-დან წამოიღეთ .getItem()-ის დახმარებით მნიშვნელობები და შეინახეთ შესაბამისს ცვლადებში. ბოლოს დაბეჭდეთ ყველა ცვლადის შიგთავსი ;>

//9) .clear() ფუნქციის დახმარებით გაასუფთავეთ თქვენი localStorage()

//10) შეინახეთ კვლავ 2 ახალი მნიშვნელობა localStorage-ში და დაბეჭდეთ მათი key-ები index-ების მეშვეობით .key() ფუნქციის დახმარებით.


//1


for (let i = 1; i <= 76; i++) {
  if (i % 2 !== 0) {
    console.log(i);
  }
}




//2
let person = {
  name: "Nika",
  age: 21,
  city: "Tbilisi",
  hobby: "Coding"
};

for (let key in person) {
  console.log(key + ":", person[key]);
}


//3
let fruits = ["apple", "banana", "mango", "orange", "kiwi", "peach"];

for (let fruit of fruits) {
  console.log(fruit);
}



//4
//localStorage არის ბრაუზერის მეხსიერება, რომელიც საშუალებას გვაძლევს
//შევინახოთ მონაცემები მუდმივად (მხოლოდ კონკრეტულ ბრაუზერში).
//მონაცემები არ ქრება გვერდის გადატვირთვის შემდეგ.

//მისი ძირითადი მეთოდებია:
 // - setItem(key, value): ამატებს ან აახლებს მნიშვნელობას storage-ში.
 // - getItem(key): აბრუნებს მითითებული key-ის მნიშვნელობას.
  //- removeItem(key): შლის კონკრეტულ მნიშვნელობას key-ის მიხედვით.
  //- clear(): ასუფთავებს მთელ localStorage-ს.
  //- key(index): აბრუნებს index-ით მითითებულ key-ს.
  //- length: აბრუნებს localStorage-ში შენახული ელემენტების რაოდენობას.



//5
 localStorage.setItem("name", "Nika");
localStorage.setItem("surname", "Beridze");
localStorage.setItem("age", "21");
localStorage.setItem("country", "Georgia");
localStorage.setItem("language", "JavaScript");
localStorage.setItem("sport", "Football");
localStorage.setItem("movie", "Inception");

console.log(setItem)



//6
localStorage.removeItem("sport");
localStorage.removeItem("movie");

console.log(removeItem)


//7
console.log("localStorage length:", localStorage.length);



//8
let myName = localStorage.getItem("name");
let myAge = localStorage.getItem("age");
let myCountry = localStorage.getItem("country");
let myHobby = localStorage.getItem("hobby");
let myLanguage = localStorage.getItem("language");

console.log(myName, myAge, myCountry, myHobby, myLanguage);





//9
localStorage.clear();


//10
localStorage.setItem("university", "Tbilisi State University");
localStorage.setItem("major", "Computer Science");

console.log(localStorage.key(0));
console.log(localStorage.key(1));
