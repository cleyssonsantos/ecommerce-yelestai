$(document).ready(function () {
    $.ajax({
      type: "GET",
      url: "http://localhost:5000/produto/buscar",
      dataType: "json",
      success: function (response) {
        console.log(response)
        
        $("#produtos").html("");
        $.each(response, function (indexInArray, value) { 
          url = "detalhes.html?"+value.id_produto
          $("#produtos").append(`<div class="col-md-4">
                                <a href="`+url+`"><img src="`+value.url_img+`" class="img-responsive"></a>
                                <p class="texto-catalogo"><a href="`+url+`" class="btn-catalogo">`+value.nome+`<br> R$ `+value.preco+`</a></p>
                                </div>`);
        });
      }
    });
  });