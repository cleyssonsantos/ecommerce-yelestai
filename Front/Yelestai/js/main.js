$(document).ready(function () {
    var name = sessionStorage.getItem('nome')
    var email = sessionStorage.getItem('email')
    console.log(name, email)
    if(name != null){
      $('.inscrevase').addClass('hidden');
      $('.entrar').addClass('hidden');
      $('.nome').removeClass('hidden');
      $("#nomeuser").html('Olá, '+name+'.');
      $('.sair').removeClass('hidden');
      $('.pedidorealizado').removeClass('hidden');
    }
    $("#sair").click(function (e) { 
      e.preventDefault();
      sessionStorage.clear()
      $(location).attr("href", "./index.html")
      
    });
});
