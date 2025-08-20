 let form = document.getElementById("registerForm");
    let registerPage = document.getElementById("registerPage");
    let mainPage = document.getElementById("mainPage");

    form.addEventListener("submit", function(event) {
        event.preventDefault(); 
        let name = document.getElementById("name").value;

        let initials = name.split(" ").map(n => n[0].toUpperCase()).join("");
        console.log("Your initials are:", initials);

        registerPage.style.display = "none";
        mainPage.style.display = "block";
    });

    let box = document.getElementById("box");

box.addEventListener("click", function() {
    box.style.borderRadius = "50%";
});

// 1
document.addEventListener("click", function(event) {
    console.log("Page clicked at:", event.clientX, event.clientY);
});

// 2
box.addEventListener("mouseover", function(event) {
    console.log("Mouse entered the div. Target:", event.target.id);
});

// 3
box.addEventListener("mouseout", function(event) {
    console.log("Mouse left the div.");
});

// 4
document.addEventListener("keydown", function(event) {
    console.log("Key pressed:", event.key);
});

// 5
box.addEventListener("dblclick", function(event) {
    console.log("Div was double-clicked!");
});
