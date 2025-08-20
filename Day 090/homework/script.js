let form = document.getElementById("registerForm");

document.getElementById("checkBtn").addEventListener("click", function() {
    console.log("Button clicked!");
});

form.addEventListener("submit", function(event) {
    event.preventDefault();
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    console.log("You have successfully registered!");
    console.log("Name:", name);
    console.log("Email:", email);
    console.log("Password:", password);
});
