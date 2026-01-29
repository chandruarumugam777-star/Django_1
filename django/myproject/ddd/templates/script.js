// Handle Learn Button Click
document.getElementById("learnBtn").addEventListener("click", function () {
    alert("Welcome! This button works using JavaScript.");
});

// Handle Submit Button
document.getElementById("submitBtn").addEventListener("click", function () {
    let username = document.getElementById("nameInput").value;

    if (username.trim() === "") {
        document.getElementById("outputText").innerHTML = "Please enter your name.";
        document.getElementById("outputText").style.color = "red";
    } else {
        document.getElementById("outputText").innerHTML = "Hello, " + username + "!";
        document.getElementById("outputText").style.color = "green";
    }
});
