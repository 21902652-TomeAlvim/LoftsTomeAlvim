document.addEventListener('DOMContentLoaded', () => {
    document.querySelector("#login_button").addEventListener('click', login_button, false)
    document.querySelector("#sign_up_button").addEventListener('click', signup_click, false)
});

function login_button() {
    document.querySelector("#login").style.display = "block";
    document.querySelector("#signup").style.display = "none";
}

function signup_click() {
    document.querySelector("#login").style.display = "none";
    document.querySelector("#signup").style.display = "block"; 
}