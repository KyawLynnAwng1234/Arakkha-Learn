document.getElementById('togglePassword').addEventListener('click', function () {
    const passwordInput = document.getElementById('password');
    
    // 1. Toggle the input field type between password and text
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        
        // 2. Change icon from eye-slash (hidden) to eye (visible)
        this.classList.remove('fa-eye-slash');
        this.classList.add('fa-eye');
    } else {
        passwordInput.type = 'password';
        
        // 3. Change icon back to eye-slash
        this.classList.remove('fa-eye');
        this.classList.add('fa-eye-slash');
    }
});