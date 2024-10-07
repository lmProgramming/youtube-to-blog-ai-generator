document.getElementById('signupForm')?.addEventListener('submit', function(event: Event) {
    event.preventDefault(); // Prevent form submission

    const usernameElement = document.getElementById('username') as HTMLInputElement | null;
    const emailElement = document.getElementById('email') as HTMLInputElement | null;
    const passwordElement = document.getElementById('password') as HTMLInputElement | null;
    const repeatPasswordElement = document.getElementById('repeatPassword') as HTMLInputElement | null;

    if (!usernameElement || !emailElement || !passwordElement || !repeatPasswordElement) {
        alert('Some form elements are missing.');
        return;
    }

    const username = usernameElement.value;
    const email = emailElement.value;
    const password = passwordElement.value;
    const repeatPassword = repeatPasswordElement.value;

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
    const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
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
    (this as HTMLFormElement).submit();
});