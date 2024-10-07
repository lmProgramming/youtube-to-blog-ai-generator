"use strict";
var _a;
(_a = document.getElementById('signupForm')) === null || _a === void 0 ? void 0 : _a.addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form submission
    var usernameElement = document.getElementById('username');
    var emailElement = document.getElementById('email');
    var passwordElement = document.getElementById('password');
    var repeatPasswordElement = document.getElementById('repeatPassword');
    if (!usernameElement || !emailElement || !passwordElement || !repeatPasswordElement) {
        alert('Some form elements are missing.');
        return;
    }
    var username = usernameElement.value;
    var email = emailElement.value;
    var password = passwordElement.value;
    var repeatPassword = repeatPasswordElement.value;
    // Validate username
    if (username.trim() === '') {
        alert('Username is required.');
        return;
    }
    // Validate email
    if (email.trim() === '') {
        alert('Email is required.');
        return;
    }
    // Validate password
    var passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
    if (!passwordRegex.test(password)) {
        alert('Password must be at least 8 characters long, contain at least one letter, one digit, and one special character.');
        return;
    }
    // Validate repeat password
    if (password !== repeatPassword) {
        alert('Passwords do not match.');
        return;
    }
    // If all validations pass, submit the form
    this.submit();
});
