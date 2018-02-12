function signIn () {
    var username = $('#sign_in_username').val();
    var password = $('#sign_in_password').val();
    console.log(username);
    console.log(password);
}

function register () {
    var username = $('#registration_username').val();
    var password = $('#registration_password').val();
    var email = $('#registration_email').val();
    console.log(username);
    console.log(password);
    console.log(email);
}

function validate () {
    var username = $('#code_username').val();
    var code = $('#code_code').val();
    console.log(username);
    console.log(code);
}

function signOut () {
    console.log('sign out');
}
