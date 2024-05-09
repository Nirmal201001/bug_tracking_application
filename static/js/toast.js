function showToast() {  
    const toastContainer = document.querySelector('.toast-messages');
    toastContainer.classList.remove('hide-toast');
    
    setTimeout(function(){
        toastContainer.classList.add('hide-toast');
    }, 2600);
}