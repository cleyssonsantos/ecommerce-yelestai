$(document).ready(function () {
    if (sessionStorage.getItem('nome') == null){
        $(location).attr('href', './login_cadastro.html')
      }
});

