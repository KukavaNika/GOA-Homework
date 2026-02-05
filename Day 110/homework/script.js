




//1
let numbers = [1, 2, 3, 4, 5];

numbers.forEach(function(num) {
  console.log(num);
});

//2
numbers.forEach(function(num) {
  console.log(num * num);
});

//3
let names = ["Nika", "Ana", "Giorgi"];

names.forEach(function(name) {
  console.log("hello " + name);
});


//4
numbers.forEach(function(num, index) {
  console.log(num + index);
});

//5
let animals = ["dog", "cat", "lion", "tiger"];

animals.forEach(function(animal, index) {
  console.log(index + ": " + animal);
});
 
//6
let animalSounds = [
  { animal: "dog", sound: "bark" },
  { animal: "cat", sound: "meow" },
  { animal: "cow", sound: "moo" }
];

animalSounds.forEach(function(item) {
  let div = document.createElement("div");
  let p = document.createElement("p");

  p.textContent = item.animal + " says " + item.sound;

  div.appendChild(p);
  document.body.appendChild(div);
});
 