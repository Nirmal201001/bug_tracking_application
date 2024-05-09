const togglePassword = document.querySelector('#togglePassword0');
const password = document.querySelector('#exampleInputPassword0');

  togglePassword.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('mdi-eye-off')
    this.classList.toggle('mdi-eye');
});

const togglePassword1 = document.querySelector('#togglePassword1');
const password1 = document.querySelector('#exampleInputPassword1');

  togglePassword1.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password1.getAttribute('type') === 'password' ? 'text' : 'password';
    password1.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('mdi-eye-off')
    this.classList.toggle('mdi-eye');
});

const togglePassword2 = document.querySelector('#togglePassword2');
const password2 = document.querySelector('#exampleInputPassword2');

  togglePassword2.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password2.getAttribute('type') === 'password' ? 'text' : 'password';
    password2.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('mdi-eye-off')
    this.classList.toggle('mdi-eye');
});