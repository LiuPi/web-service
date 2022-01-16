function validateUserName(name) {
    const nameRegex = /^[a-zA-Z\-]+$/;
    return name.match(nameRegex);
};

function validateEmail(email) {
    const emailRegex =
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return email.match(emailRegex);
};

function validateForm() {
    let message = "";
    let result = true;

    let enteredName = document.forms["formHello"]["username"].value;
    let enteredSurname = document.forms["formHello"]["usersurname"].value;
    let enteredEmail = document.forms["formHello"]["useremail"].value;

    if (enteredName.trim().length === 0 || !validateUserName(enteredName)) {
        message = "Please enter a valid name";
        result = false;
    }

    if (enteredSurname.trim().length === 0 || !validateUserName(enteredSurname)) {
        message = "Please enter a valid surname";
        result = false;
    }

    if (enteredEmail.trim().length === 0 || !validateEmail(enteredEmail)) {
        message = "Please enter a valid email address";
        result = false;
    }

    document.getElementById("message").innerHTML = message;

    return result;

  }